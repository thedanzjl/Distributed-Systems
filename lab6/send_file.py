from tqdm import tqdm
import argparse
import socket
import os


def send_file(file_name, host_name, port):
    file = open(file_name, "rb")
    s = socket.socket()
    s.connect((host_name, port))
    s.send(bytes(file_name + ("|" * (32 - len(file_name))), "utf-8"))
    p = file.read(1024)

    size = os.path.getsize(file_name)
    for _ in tqdm(range((size // 1024) + 1)):
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
    send_file(args.file_name, args.host_name, args.port)
