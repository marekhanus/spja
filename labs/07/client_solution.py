import socket
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python client.py <server> <port>")
        exit(1)

    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    while True:
        line = input()
        if line == "end":
            client.close()
            break
        client.sendall("{}\n".format(line).encode())
        data = client.recv(512)
        if not data:
            print("Server disconnected")
            break
        print("Result: {}".format(data.decode().strip()))
