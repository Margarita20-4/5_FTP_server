import socket
import time


def sign_in():
    sock = socket.socket()
    sock.connect(("127.0.0.1", 9091))
    sock.recv(1024 * 16)
    sock.send("test".encode())
    sock.recv(1024 * 16)
    sock.send("qwerty123".encode())
    sock.recv(1024 * 16)
    main(sock)


def main(sock):
    tests = [("pwd", "\\"),
             ("ls", ""),
             ("mkdir rita1", ""),
             ("touch rita1", ""),
             ("mv rita1.txt rita1", ""),
             ("touch rita1", ""),
             ("rm rita1.txt", ""),
             ("cd rita1", ""),
             ("mv rita1.txt rita2.txt", ""),
             ("write rita2.txt qwerty", ""),
             ("cat 2.txt", "qwerty")]
    for index, test in enumerate(tests):
        request = test[0]
        sock.send(request.encode())
        time.sleep(0.1)
        res = sock.recv(1024).decode()
        response = "\n".join(res.split("\n")[:-1])
        print("•" * 50)
        print(f"Проверка {index + 1}")
        print(f"Ввели: {test[0]}")
        print(f"Полученный результат: {response}")
        print(f"Ожидаемый результат: {test[1]}")
        print(f"Тест {'' if response == test[1] else 'не'}корректный")
        print("•" * 50 + "\n")


if __name__ == '__main__':
    sign_in()