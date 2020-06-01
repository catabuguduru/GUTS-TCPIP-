def get_path(self, child_directory):
        """
            Return path string to print.

            Parameters -
            ---------------------------
            child_directory - String of subdirectory in which user is present

            Returns -
            -------------------------
            String
        """
        extra_string = os.path.realpath(os.path.abspath(SERVER_DATABASE))
        return str(os.path.realpath(os.path.abspath(child_directory))).replace(extra_string, "")


class FileHandlerClient(FileHandlerHelper):
    """
        FileHandlerClient for every user

        Attributes -
        ----------------------
        username : Username of user if logged in

        rights : Bool for admin rights

        read_file_name : File name of opened file object

        read_file_object : File object of opened file.

        child_directory : current directory

        thread : Thread object if started

        password : Password of logged in user

        Methods -
        ----------------------
        handle_client() : Start a thread for client

        command_formatter(command) : Format a command properly

        commands(username, connection) : Check commands

        show_commands() : Returns a string of list of commands

        register_user(username, password, rights) : Register a new user

        login_user(username, password) : Login function

        write_file(filename, contents, clear_content=False) : Write a file

        read_file(filename, close_file=False) : Read a file

        list() : Returns a list of all files and folders in directory

        create_folder(folder) : Create a new folder

        change_folder(folder) : Change the folder

        delete(username, password) : Delete user

        delete_user(username) : Helper to delete the user
    """

    def __init__(self):
        """
            Declare attributes
        """
        self.username = None
        self.rights = False
        self.read_file_name = None
        self.read_file_object = None
        self.child_directory = os.path.join(SERVER_DATABASE)
        self.thread = None
        self.password = None

    def handle_client(self, connection):
        """
            Start a thread to contact with client

            Parameters -
            ---------------------------
            connection - socket connection

        """
        self.thread = threading.Thread(
            target=self.commands, args=(connection, ), daemon=True)
        self.thread.start()

