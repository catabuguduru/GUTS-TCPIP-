class TestRegisterUser(unittest.TestCase):
    """
        Unittest class for register user command
    """

    def test_register_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("register"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_register_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        user = ''.join(random.choice(string.ascii_lowercase)
                       for i in range(8))
        server.send(str.encode("register %s password" % user))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_register_and_login(self):
        """
            Reasoning -
            ------------------
            Can register and login
        """
        server = connect_server("127.0.0.1", 8081)
        user = ''.join(random.choice(string.ascii_lowercase)
                       for i in range(8))
        server.send(str.encode("register %s password admin" % user))
        server.recv(10000)
        self.assertTrue(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        server.send(str.encode("login %s password" % user))
        response = str(server.recv(10000), "utf-8")
        server.close()
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete %s password" % user))
        server.recv(10000)
        server.close()
        self.assertFalse(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        self.assertEqual('Login completed.', response)
        class TestDeleteUser(unittest.TestCase):
    """
        Unittest class for delete user command
    """

    def test_login_required(self):
        """
            Reasoning -
            ------------------
            Login is required to execute this command
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("delete testing_user_2 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login Please.', response)

    def test_delete_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_delete_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2 password blah blah"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_delete_wrong_username(self):
        """
            Reasoning -
            ------------------
            Check for wrong username
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode(
            "delete testing_user_22313131893u18931931 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Username not found.', response)

    def test_delete_wrong_password(self):
        """
            Reasoning -
            ------------------
            Check for wrong password
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2 password_wrong"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Wrong password', response)

    def test_delete_and_register_again(self):
        """
            Reasoning -
            ------------------
            Test delete and register the user again
        """
        server = connect_server("127.0.0.1", 8081)
        user = ''.join(random.choice(string.ascii_lowercase)
                       for i in range(8))
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("register %s password admin" % user))
        server.recv(10000)
        self.assertTrue(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        server.send(str.encode("delete %s password" % user))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertFalse(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        self.assertEqual('Delete user.', response)
class TestDeleteUser(unittest.TestCase):
    """
        Unittest class for delete user command
    """

    def test_login_required(self):
        """
            Reasoning -
            ------------------
            Login is required to execute this command
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("delete testing_user_2 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login Please.', response)

    def test_delete_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_delete_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2 password blah blah"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_delete_wrong_username(self):
        """
            Reasoning -
            ------------------
            Check for wrong username
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode(
            "delete testing_user_22313131893u18931931 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Username not found.', response)

    def test_delete_wrong_password(self):
        """
            Reasoning -
            ------------------
            Check for wrong password
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2 password_wrong"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Wrong password', response)

    def test_delete_and_register_again(self):
        """
            Reasoning -
            ------------------
            Test delete and register the user again
        """
        server = connect_server("127.0.0.1", 8081)
        user = ''.join(random.choice(string.ascii_lowercase)
                       for i in range(8))
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("register %s password admin" % user))
        server.recv(10000)
        self.assertTrue(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        server.send(str.encode("delete %s password" % user))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertFalse(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        self.assertEqual('Delete user.', response)
class TestDeleteUser(unittest.TestCase):
    """
        Unittest class for delete user command
    """

    def test_login_required(self):
        """
            Reasoning -
            ------------------
            Login is required to execute this command
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("delete testing_user_2 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Login Please.', response)

    def test_delete_less_arguments(self):
        """
            Reasoning -
            ------------------
            Check for less arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_delete_more_arguments(self):
        """
            Reasoning -
            ------------------
            Check for more arguments
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2 password blah blah"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Check arguments', response)

    def test_delete_wrong_username(self):
        """
            Reasoning -
            ------------------
            Check for wrong username
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode(
            "delete testing_user_22313131893u18931931 password"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Username not found.', response)

    def test_delete_wrong_password(self):
        """
            Reasoning -
            ------------------
            Check for wrong password
        """
        server = connect_server("127.0.0.1", 8081)
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("delete testing_user_2 password_wrong"))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertEqual('Wrong password', response)

    def test_delete_and_register_again(self):
        """
            Reasoning -
            ------------------
            Test delete and register the user again
        """
        server = connect_server("127.0.0.1", 8081)
        user = ''.join(random.choice(string.ascii_lowercase)
                       for i in range(8))
        server.send(str.encode("login testing_user password"))
        server.recv(10000)
        server.send(str.encode("register %s password admin" % user))
        server.recv(10000)
        self.assertTrue(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        server.send(str.encode("delete %s password" % user))
        response = str(server.recv(10000), "utf-8")
        server.close()
        self.assertFalse(os.path.exists(os.path.join(SERVER_DATABASE, user)))
        self.assertEqual('Delete user.', response)



