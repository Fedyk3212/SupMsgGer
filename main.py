import json
import socket
import time
from threading import Thread

import art
from colorama import Fore
from colorama import Style


# Главная Функция
def maindef():
    print("\033[H\033[J")
    print(Fore.BLUE)
    artsd = ("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠁⠄⠄⠄⠄⠈⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣇⠄⠄⠄⢀⣀⣀⣀⠄⠄⠄⠄⠄⢀⣀⣀⣀⡀⠄⠄⢠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡄⠄⣼⣿⣿⣿⣿⣷⠄⠄⠄⢀⣿⣿⣿⣿⣿⠄⠄⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠄⠹⣿⣿⣿⣿⠏⣰⣿⣷⡀⢿⣿⣿⣿⡿⠄⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠄⠄⠉⠛⠛⠁⢠⣿⣿⣿⣷⠄⠙⠛⠋⠄⠄⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣄⣀⡀⠄⠄⠄⠈⠛⠋⠙⠋⠄⠄⠄⠄⣀⣀⣸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⡄⠄⢀⡀⣀⠄⠄⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣧⣿⣿⣟⣿⢸⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⡏⠿⢿⡿⣿⠛⠏⢿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠈⠁⠄⠄⠄⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢻⣿⣿⣿⣿
⣿⣿⣿⣿⠁⠄⠄⠄⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠄⠄⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣧⣤⣶⣶⣶⣦⣄⠈⠙⠿⣿⣿⣿⡿⠟⠋⢁⣀⣀⣀⠄⢠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⠄⠉⠁⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣠⣴⣶⣶⣤⣌⡙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠟⢋⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣈⠙⠻⢿⣿⣿⣿⣿
⠟⠛⠛⠛⠋⣁⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠄⠄⠄⣨
⣷⡄⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⣼⣿
⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """)
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
    elif mode == "debug":
        print(Fore.RED)
        print(artsd)
        quit()
    else:
        print("Вы ввели неверную команду")
    maindef()


# Клиентский код
def clientmode():
    conf_reload_update()
    settings = conf_reload_update()
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
    print("Введите сообщение")
    t2 = Thread(target=messege_receve, args=(client,))
    t2.start()
    client.send(str("/nick " + settings["nickname"]).encode('utf-8'))
    while True:
        message = input()
        if message == "":
            continue
        client.send(message.encode('utf-8'))
        cmd = message.split()

        name = cmd[0]
        if name == "/quit":
            client.close()
            maindef()

# Списки подключений и ников
conns = []
nicks = {}


def messege_receve(client):
    while True:
        server = client.recv(1024).decode('utf8')
        print(server)


# Серверный код
def servermode():
    conf_reload_update()
    settings = conf_reload_update()
    serverhost = (settings["server_ip"], settings["server_port"])
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
            print(Fore.RED + "Нерпавильно настроен IP или Порт")
            time.sleep(3)
            maindef()
        # Запуск сервер
        server.listen(settings["max_peoples"])
        print("Жду запрос на подключение")
        while True:
            # сообщения для сервера и от сервера
            msg = "Подключен"
            conn, addr = server.accept()
            nicks[addr] = "User" + str(len(nicks))
            thread = Thread(target=dataprinting, args=(conn, addr))
            thread.start()
            conns.append(conn)
            print(msg, addr)


def dataprinting(conn: socket.socket, addr):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data[0] == "/":
            cmd = data.split()
            if cmd[0] == "/nick" and len(cmd) == 2:
                nicks[addr] = cmd[1]

        else:
            msg = nicks[addr] + ": " + data
            print(msg)
            for conn2 in conns:
                try:
                    conn2.send(str(msg).encode('utf-8'))
                except BrokenPipeError:
                    conns.remove(conn2)
                    print("Клиент Отключился")


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
