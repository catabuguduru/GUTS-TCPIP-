
    def test_login_wrong_username(self):
        """
            Reasoning -
            ------------------
            Wrong username response
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user2 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Username not found. Please register.', response)

    def test_login_wrong_password(self):
        """
            Reasoning -
            ------------------
            Check for wrong password
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password2"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Wrong password.', response)

    def test_login_wrong_username_wrong_password(self):
        """
            Reasoning -
            ------------------
            Check for both wrong username and password
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user2 password2"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Username not found. Please register.', response)

    def test_login_correct(self):
        """
            Reasoning -
            ------------------
            Successfull login for testing_user
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login completed.', response)

    def test_login_correct_second_user(self):
        """
            Reasoning -
            ------------------
            Successfull login for testing_user_2
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user_2 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login completed.', response)


class TestChangeDirectory(unittest.TestCase):
    """
        Unittest class for testing change folder command.
    """

    def test_login_required(self):
        """
            Reasoning -
            ------------------
            Login required for the command
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("change_folder folder"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login Please.', response)
