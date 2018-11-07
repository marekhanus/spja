import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 server.py <port>")
        exit(1)

    """
    3 points.

    Create an application with CMD parameter `port`.
    1) Create a TCP server listening at 127.0.0.1:port
    2) Start listening for TCP connections
        - after a connection is initiated:
            - print "Received connection from: <client-address>"
            - create a new thread that will handle the connection
        - on a keyboard interrupt, print "Server exiting" and exit the program
    3) For each client connection:
        - read lines from client, for each line:
            - if line is in the form <number> +-*/ <number> (e.g. 5+5, 13*8 etc.),
              evaluate the expression and send the result to the client (followed by a newline)
            - if the line is invalid, send the line "Invalid input" to the client
            - print all client requests and responses
        - if client disconnects, print "Exited connection from: <client-address>"
    
    Example:
        $ python3 server.py 5555
        Received connection from: 127.0.0.1:55657
        Input: 5+5, output: 10
        Input: 2 * 13, output: 26
        Input: asd, output: Invalid input
        Exited connection from: 127.0.0.1:55657
        Received connection from: 127.0.0.1:55658
        Received connection from: 127.0.0.1:55659
        (Ctrl+C)
        Server exiting
    
    1 point (bonus).

    Enable the user to store variables on the server using the `=` operator 
    and then reference them in formulas. The variables will live only for the
    duration of the client connection.

    x=5
    5+x
    Result: 10
    y=3
    y*6
    Result: 18
    x=y
    x+10
    Result: 13
    """
