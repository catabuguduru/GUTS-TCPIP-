"""Client functions with its implementation"""
import socket
import sys


def connect_server(host, port):
    """
        Connect to server

        Returns -
        --------------------
        Socket connection
    """
    print("Connecting to server")
    try:
        server = socket.socket()
        server.connect((host, port))
    except ConnectionRefusedError:
        print("Server not started yet")
        sys.exit()
    print("Connection completed")
    return server


def contact_server(server, issued=[]):
    """
        Contact with server

        Parameters -
        --------------
        server - Socket connection

    """
    command = input("Enter input - ")
    command = command.lstrip(" ").rstrip(" ").split(" ")
    if command[0] == "":
        print("Enter some command")
        contact_server(server, issued=issued)
    if command[0] == "commands":
        if len(command) == 2:
            if command[1] == "issued":
                print("\n".join(issued))
                contact_server(server, issued=issued)
            elif command[1] == "clear":
                issued = []
                print("Commands cleared")
                contact_server(server, issued=issued)
        else:
            issued.append(" ".join(command))
            server.send(str.encode(" ".join(command)))
            print(str(server.recv(10000), "utf-8"))
            contact_server(server, issued=issued)
    elif command[0] == "quit":
        server.close()
        print("Closed.")
    else:
        issued.append(" ".join(command))
        server.send(str.encode(" ".join(command)))
        print(str(server.recv(10000), "utf-8"))
        contact_server(server, issued=issued)


if __name__ == "__main__":
    server = connect_server("127.0.0.1", 8080)
    print("Enter commands for help.")
    contact_server(server)
