"""Server handler base class with inheritance of filehandler class"""

import os
import socket
import sys
import threading
import datetime
import shutil

USERS = []

SERVER_DATABASE = "files/"


class FileHandlerHelper:
    """
        Helper functions class

        Methods -
        ----------------------
        read_logins() : returns the login users dataset

        isexistandisfile(child_directory, filename) : True if the file exists and it is a file.

        allowed_folder(username, child_directory, folder) : True if user changes to new allowed location.

        get_path(child_directory) : return path string to print.
    """

    def read_logins(self):
        """
            Returns the login users dataset

        """
        with open(os.path.join(SERVER_DATABASE, 'login'), 'r') as data:
            content = data.read()
        content = content.lstrip("\n").rstrip("\n")
        return content

    def isexistandisfile(self, child_directory, filename):
        """
            True if the file exists and it is a file.

            Parameters -
            ---------------------------
            child_directory - String of subdirectory in which user is present

            filename - Filename to be checked

            Returns -
            -------------------------
            Bool
        """
        return os.path.exists(os.path.join(child_directory, filename)) and os.path.isfile(os.path.join(child_directory, filename))

    def allowed_folder(self, username, child_directory, folder):
        """
            True if user changes to new allowed location.

            Parameters -
            ---------------------------
            username - Username of the user.

            child_directory - String of subdirectory in which user is present

            filename - Filename to be checked

            Returns -
            -------------------------
            Bool
        """
        parent_string = os.path.realpath(os.path.abspath(
            os.path.join(SERVER_DATABASE, username)))
        child_string = os.path.realpath(os.path.abspath(
            os.path.join(child_directory, folder)))
        return parent_string in child_string
