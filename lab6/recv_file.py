import socket
import sys
import os

# s = socket.socket()
# s.bind("localhost", 8000)
# s.listen(3)


def name_manager(file_name):
    """
    Checks if this file name is already in use. In this case adds in the end of file _copy with number
    :returns: updated file name
    """
    name, ext = file_name.split(".")
    if file_name in os.listdir(os.curdir):
        if name[:-1].endswith("copy"):
            copy_num = int(name[-1]) + 1
            return "{}{}.{}".format(name[:-1], copy_num, ext)
        else:
            return "{}_copy1.{}".format(name, ext)
    else:
        return file_name


def recv_file():
    while True:
        client_socket, address = s.accept()
        file_name = client_socket.recv(32)
        f = open(name_manager(file_name), 'wb')
        while True:
            p = client_socket.recv(1024)
            while p:
                    f.write(p)
                    p = sc.recv(1024)
        f.close()


        client_socket.close()

    s.close()


if __name__ == '__main__':
    recv_file()
