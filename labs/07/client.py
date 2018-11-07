import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 client.py <server> <port>")
        exit(1)

    """
    2 points.

    Create an application with CMD parameters `server` and `port`.
    1) Connect to the TCP server
    2) Read lines from the input (terminal).
        - when the user enters "end", close the socket and exit the program
        - otherwise send the user's input to the server and print the response prepended by "Result: "
    3) If the server disconnects, print "Server disconnected" and exit the program

    Example:
        $ python3 client.py 127.0.0.1 5555
        5+5
        Result: 10
        2 * 13
        Result: 26
        asd
        Result: Invalid input
    """
