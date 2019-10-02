import socket
import os

PORT = 8888


def name_manager(file_name, dec=True):
    """
    Checks if this file name is already in use. In this case adds "copy" in the end of the file name with relative
    number of copy.
    :param dec: do we need to decode from bytes to string?
    :returns: updated file name
    """
    if dec:
        file_name = file_name.decode("utf-8")
    file_name = file_name.replace("|", "")
    name, ext = file_name.split(".")
    if file_name in os.listdir(os.curdir):
        print('1')
        if name[:-1].endswith('copy'):
            print(2)
            copy_n = int(name[-1]) + 1
            result = "{}{}.{}".format(name[:-1], copy_n, ext)
        else:
            print(3)
            result = "{}_copy1.{}".format(name, ext)
            if result in os.listdir(os.curdir):
                return name_manager(result, dec=False)
    else:
        print(4)
        result = file_name
    print('received file: %s' % result)
    return bytes(result, "utf-8")


def recv_file():
    print("hosted on port %i ...." % PORT)
    s = socket.socket()
    s.bind(("", PORT))
    s.listen(3)
    while True:
        client_socket, address = s.accept()
        print("accepted new connection: ", address)
        file_name = client_socket.recv(32)
        if not file_name:
            continue
        f = open(name_manager(file_name), 'wb')
        while True:
            p = client_socket.recv(1024)
            while p:
                    f.write(p)
                    p = client_socket.recv(1024)
        f.close()

        client_socket.close()

    s.close()


if __name__ == '__main__':
    recv_file()
