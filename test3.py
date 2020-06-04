 def test_cd_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("change_folder"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_cd_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("change_folder folder password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_cd_wrong_foldername(self):
        """
            Reasoning -
            ------------------
            Check for wrong folder name
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("change_folder folder_wrong"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual("Destination folder doesn't exists.", response)

    def test_cd_above_root(self):
        """
            Reasoning -
            ------------------
            Change folder to above root
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("change_folder .."))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual("Permission Denied.", response)

    def test_cd_correct(self):
        """
            Reasoning -
            ------------------
            Change folder correctly
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("change_folder folder"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual(r"Changed folder to \testing_user\folder", response)


class TestReadFile(unittest.TestCase):
    """
        Unittest class for read file command
    """
