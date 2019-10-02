import argparse
import socket


def send_file(file_name, host_name, port):
    file = open(file_name, "rb")
    s = socket.socket()
    s.connect((host_name, port))
    s.send(file_name)
    p = file.read(1024)
    while p:
        s.send(p)
        p = file.read(1024)
    s.close()
    file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str)
    parser.add_argument("host_name", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    send_file(parser.file_name, parser.host_name, parser.port)
