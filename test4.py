 def test_login_required(self):
        """
            Reasoning -
            ------------------
            Login required to use this command
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("read_file testing.txt"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login Please.', response)

    def test_read_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("read_file"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Closed file.', response)

    def test_read_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("read_file testing.txt blah blah"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_read_wrong_filename(self):
        """
            Reasoning -
            ------------------
            Check for wrong filename
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("read_file testing_wrong.txt"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual("testing_wrong.txt doesn't exist", response)

    def test_read_correct(self):
        """
            Reasoning -
            ------------------
            Check for proper read
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("read_file testing.txt"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual(
            "testingtestingtestingtestingtestingtestingtesting", response)

    def test_read_close(self):
        """
            Reasoning -
            ------------------
            Close file properly.
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("read_file testing.txt"))
        server.recv(10000)
        server.send(str.encode("read_file"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual(r"Closed file.", response)


class TestWriteFile(unittest.TestCase):
    """
        Unittest class to check write file command.
    """

    def test_login_required(self):
        """
            Reasoning -
            ------------------
            Check login required
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("write_file write_testing.txt data"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login Please.', response)

    def test_write_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("write_file"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_write_clear_file(self):
        """
            Reasoning -
            ------------------
            Check to clear the file contents
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("write_file write_testing.txt"))
        server.recv(10000)
        server.send(str.encode("read_file write_testing.txt"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual(
            "Empty file.", response)

    def test_write_correct(self):
        """
            Reasoning -
            ------------------
            Check if file gets written
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("write_file write_testing.txt abcd"))
        server.recv(10000)
        server.send(str.encode("read_file write_testing.txt"))
        response = str(server.recv(10000), "utf-8")
        server.send(str.encode("write_file write_testing.txt"))
        server.recv(10000)
        server.close()
        self.assertEqual(
            "\nabcd", response)

