import socket
import threading

class server_main():

    def __init__(self):
        self.s = None
        self.connections = []
        self.ips = []
        self.threads = {}
        self.workers = {}

    def socket_job(self):
        """
        Create a socket and start accepting connections asyncronysly
        """
        try:
            self.s = socket.socket()
            self.s.bind(("", 8080))
            self.s.listen(5)
            print("Server opened at port 8080")
        except socket.error as msg:
            print("error: " + str(msg))
        while True:
            try:
                conn, address = self.s.accept()
                self.s.setblocking(1)
                self.connections.append(conn)
                self.ips.append(address)
                self.threads[address] = False
                # attach a worker to ip
                self.workers[address] = Worker(address)
                print("Client connected from ip :" + address[0])
            except:
                print("Error")
