import json
import socket
import time

import art
from colorama import Fore
from colorama import Style


def maindef():
    print(Fore.BLUE)
    art.tprint("SupMESGER")
    print(Fore.BLUE + "Made by Fedyk 3212")
    print("\n")
    print(Fore.GREEN + 'Сhoose your mode')
    print(Fore.YELLOW + 'Cliet 1)     Admin/Server 2)    CommandList 3)     Quit 4)    Settings 5)')
    mode = (input())
    if mode == "1":
        clientmode()
    elif mode == "2":
        servermode()
    elif mode == "3":
        print("Client commands["
              "/nick: Choose/Change Your Nickname"
              "/quit: Quit in Menu")
        cmd = input()
        if cmd == "quit":
            maindef()
    elif mode == "4":
        quit()
    elif mode == "5":
        try:
            cofig["max_peoples"] = int(read_or_default("Введите максимальное количество человек в чате", "max_peoples"))
        except TypeError:
            print(Fore.RED + "Вводите пожалуйста только цифры")
            time.sleep(3)
            maindef()
        cofig["server_port"] = int(read_or_default("Введите порт сервера", "server_port"))
        cofig["server_ip"] = read_or_default("Введите IP сервера", "server_ip")
        cofig["nickname"] = read_or_default("Введите Никнейм", "nickname")
        with open("config.json", "w") as f:
            json.dump(cofig, f)
        maindef()
    else:
        print("Вы ввели неверную команду")
    maindef()


# Клиентский код
def clientmode():
    conf_reload_update()
    data = conf_reload_update()
    niknames = data["nickname"]
    print("Write Ip address to connect(default localhost)")
    ip = str(input())
    if ip == "localhost":
        ip = "127.0.0.1"
    elif ip is None:
        ip = "127.0.0.1"
    port = int(read_or_default("Write Port to connect (default 65433)", "server_port"))
    hostclient = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(hostclient)
    except ConnectionRefusedError:
        print(Fore.RED + "Возникла ошибка при подключении перепроверьте данные Или запустите сервер")
        print(Style.RESET_ALL)
        print('3s')
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('\a')
        maindef()
    while True:
        while True:
            print("Введите сообщение")
            message = input()
            finmesg = (niknames + ": " + message)
            client.send(finmesg.encode('utf-8'))
            if message == "quit":
                client.close()
                maindef()
            elif message == "/nick":
                niknames = input()


# Серверный код
def servermode():
    conf_reload_update()
    data = conf_reload_update()
    serverhost = (data["server_ip"], data["server_port"])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Выбор перед запуском режима сервера
        print(Fore.RED + "Во точно хотите запустить сервер Y/N")
        cmd1 = input()
        if cmd1 == "N":
            print("Выхожу из режима ожидания")
            time.sleep(1)
            maindef()
        elif cmd1 == "Y":
            print("")
        else:
            print("Неверная Команда")
            maindef()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            server.bind(serverhost)
        except OSError:
            print(Fore.RED + "Нерпавильно настрое IP или Порт")
            time.sleep(3)
            maindef()
        # Запуск сервер
        server.listen()
        flag = True
        print("Жду запрос на подключение")
        while flag:
            # сообщения для сервера и от сервера
            msg = "Подключен"
            conn, addr = server.accept()
            print(msg, addr)
            while True:
                data = conn.recv(1024)
                print(data.decode("utf-8"))


def read_or_default(name, key):
    with open("config.json", "r") as fi:
        data = json.load(fi)
    print(name)
    string = input()
    if string == "":
        return data[key]
    else:
        return string


def conf_reload_update():
    with open("config.json", "r") as fi:
        data = json.load(fi)
        return data


if __name__ == '__main__':
    cofig = {"max_peoples": 5,
             "server_port": 65433,
             "server_ip": "127.0.0.1",
             "nickname": "Username"}
    with open("config.json", "w") as file:
        json.dump(cofig, file)
        file.close()
    maindef()
