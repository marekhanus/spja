import re
import socket
import sys
import threading


def resolve(database, var):
    if var.isdigit():
        return int(var)
    elif var not in database:
        raise Exception("Invalid variable {}".format(var))
    return database[var]


def handle_arithmetic(database, l, r, op):
    l_var = resolve(database, l)
    r_var = resolve(database, r)

    if op == '+': return l_var + r_var
    if op == '-': return l_var - r_var
    if op == '*': return l_var * r_var
    if op == '/': return l_var / r_var
    raise Exception("Invalid op {}".format(op))


def handle_assign(database, l, r):
    r_var = resolve(database, r)
    database[l] = r_var
    return "{} set to {}".format(l, r_var)


def handle_line(database, line):
    regex = r'^((?:\w|\d)+)\s*{}\s*((?:\d|\w)+)$'

    ops = [
        ('^((?:\w|\d)+)$', lambda val: str(resolve(database, val))),
        (regex.format(r'\+'), lambda l, r: handle_arithmetic(database, l, r, '+')),
        (regex.format(r'-'), lambda l, r: handle_arithmetic(database, l, r, '-')),
        (regex.format(r'\*'), lambda l, r: handle_arithmetic(database, l, r, '*')),
        (regex.format(r'/'), lambda l, r: handle_arithmetic(database, l, r, '/')),
        (r'^(\w+)\s*=\s*((?:\d|\w)+)$', lambda l, r: handle_assign(database, l, r))
    ]

    for (regex, fn) in ops:
        match = re.match(regex, line)
        if match:
            left = match.group(1)
            if len(match.groups()) == 1:
                return fn(left)
            else:
                right = match.group(2)
                return fn(left, right)
    raise Exception("Invalid input: {}".format(line))


def init_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(10)
    return sock


def server_loop(client, addr):
    database = {}
    buffer = ""
    while True:
        data = client.recv(512)
        if not data:
            break
        try:
            buffer += data.decode()
        except Exception as e:
            result = str(e)
            client.sendall("{}\n".format(result).encode())
        while '\n' in buffer:
            index = buffer.index('\n')
            line = buffer[:index]
            try:
                result = handle_line(database, line)
            except Exception as e:
                result = str(e)

            print("Input: {}, output: {}".format(line, result))

            client.sendall("{}\n".format(result).encode())
            buffer = buffer[index + 1:]
    print("Exited connection from {}".format(addr))


def arithmetic_server(port):
    sock = init_server(port)

    try:
        while True:
            client, addr = sock.accept()
            print("Received connection from: {}".format(addr))

            thread = threading.Thread(target=server_loop, args=(client, addr))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("Server exiting")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        exit(1)

    PORT = int(sys.argv[1])

    print("Server listening on 127.0.0.1:{}".format(PORT))
    arithmetic_server(PORT)
