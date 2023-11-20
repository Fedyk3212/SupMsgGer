import random
import socket
import time
from threading import Thread
from art import tprint
from colorama import Fore
from colorama import Style
import requests


def main_def():
    print("\033[H\033[J")
    print(Fore.BLUE)
    tprint("Vadim_Bot")
    print(Fore.YELLOW + "1) Start 2) Instructions 3) Quit")
    cmd = input()
    if cmd == "1":
        client()
    elif cmd == "2":
        print("""
        Инструкция к IP боту
        1)Сначала запустите сервер на который вы хотите подключить бота
        2)Потом выберите функцию Start в главном меню
        3)В функции Start Сначала введите IP потом нажимите ENTER потом введите порт
        4)После подключения бота к серверу для получения списка комманд введите команду помощь
        5)Если вы хотите отключить бота пропишите в терминали бота quit и он автоматически о
        """)
        print('Введите bak чтобы вернуться обратно')
        time.sleep(5)
        main_def()
    elif cmd == "close":
        quit()
    elif cmd == "back":
        main_def()


def client():
    msg = "Я подключился теперь вы можете вводить команды для списка команд напишите !помощь в терминале клиента"
    print("Введите IP")
    ip = str(input())
    if ip is None:
        ip = "127.0.0.1"
    print("Введите порт")
    try:
        port = int(input())
    except ValueError or TypeError:
        port = 65433
    hostclient = (ip, port)
    clientbot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientbot.connect(hostclient)
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
        main_def()

    t1 = Thread(target=commandrecive, args=(clientbot,))
    t1.start()
    clientbot.send(str("/nick " + "IP_BOT").encode('utf-8'))
    print("Я успешно подключился Далее напишите команду находясь в режиме Клиент")
    clientbot.send(msg.encode('utf-8'))


def commandrecive(clientbot: socket.socket):
    while True:
        servmsg = clientbot.recv(1024).decode('utf-8')
        spilcmd = servmsg.split()
        if spilcmd[1] == "!Помощь":
            clientbot.send("""
            Мои команды:
            1) !ВычислиIP
            Пример:!ВычислиIP 46.226.227.20
            Пояснение: Функция геокодирование из IP в координаты
            2) !Рандом
            Пояснение: Сгенерирует рандомное число хз зачем
            """.encode('utf-8'))
        elif spilcmd[1] == "!Рандом":
            random_number = random.randint(0, 212121)
            clientbot.send(str(random_number).encode('utf-8'))
        elif spilcmd[1] == "!ВычислиIP":
            clientbot.send("Вычисляю".encode('utf-8'))
            time.sleep(1)
            if len(spilcmd) == 3:
                ipd = spilcmd[2]
                response = requests.get(
                    f"http://ip-api.com/json/{ipd}?lang=ru&fields=status,message,country,regionName,city,query")
                responsedict = response.json()
                if responsedict["status"] == "fail":
                    clientbot.send("Введен Неккоректный IP".encode('utf-8'))
                    continue
                else:
                    msgs = (responsedict["country"] + ": " + responsedict["regionName"] + ": " + responsedict["city"])
                    clientbot.send(str(msgs).encode('utf-8'))
            else:
                clientbot.send("Комманда не полная или введена неправильно".encode('utf-8'))
                continue


if __name__ == '__main__':
    print(Fore.LIGHTRED_EX)
    main_def()
