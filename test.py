"""
    Main testing file
"""

import unittest
import sys
import string
import random
import os
from server import ServerSocket, SERVER_DATABASE
from client import connect_server

# Server is hosted on port 8081 for testing, not to interfare with real server
ServerSocket("0.0.0.0", 8081).connect_clients_daemon()


class TestConnection(unittest.TestCase):
    """
        Unittest class for testing connection.
    """

    def test_init_server(self):
        """
            Reasoning -
            ------------------
            Client should be able to connect.
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("Commands"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertNotEqual('', response)


class TestLogin(unittest.TestCase):
    """
        Unittest class for testing login
    """

    def test_login_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_login_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password argument"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)
