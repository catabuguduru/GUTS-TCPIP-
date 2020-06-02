def delete_user(self, username):
        """
            Helper function to delete function

            Parameters -
            ---------------------------
            username - String of username

            Returns -
            ---------------------------
            Response
        """
        global USERS
        with open(os.path.join(SERVER_DATABASE, 'login'), 'r') as data:
            content = data.read()
        content = content.lstrip("\n").rstrip("\n")
        users = content.split("\n")
        users = [user.split(",") for user in users]
        new_users = []
        for user in users:
            if username != user[0]:
                new_users.append(user[0]+","+user[1]+","+user[2])
        with open(os.path.join(SERVER_DATABASE, 'login'), 'w') as data:
            data.write("\n".join(new_users))
        if username in USERS:
            # this will take case of logged in users
            USERS.remove(username)
        shutil.rmtree(os.path.join(SERVER_DATABASE, username))
        return "Username not found."


class ServerSocket:
    """
        Server socket class

        Attributes -
        ----------------------
        host : Host ip

        port : Port at which server is to be hosted

        socket_handler : Socket object

        Methods -
        ----------------------
        connect_clients() : Start connecting to clients

    """

    def __init__(self, host, port):
        """
            Start the socket binding
        """
        self.host = host
        self.port = port
        self.socket_handler = socket.socket()
        try:
            print("Starting Server")
            self.socket_handler.bind((self.host, self.port))
            self.socket_handler.listen(10)
            print("Started server successfully")
        except OSError:
            print("Error in binding socket")
            sys.exit()

    def connect_clients(self):
        """
            Connect all clients
        """
        while True:
            connection, address = self.socket_handler.accept()
            self.socket_handler.setblocking(1)
            print("Client connected from IP - ", address[0])
            FileHandlerClient().handle_client(connection)

    def connect_clients_daemon(self):
        """
            Connect all clients on daemon thread
        """
        threading.Thread(target=self.connect_clients,
                         args=(), daemon=True).start()


if __name__ == "__main__":
    SERVER_OBJECT = ServerSocket("0.0.0.0", 8080)
    SERVER_OBJECT.connect_clients()
