  def list(self):
        """
            Returns a list of files/folders

            Returns -
            ---------------------------
            Response
        """
        if self.username is None:
            return "Login Please."
        all_files_folders = os.listdir(self.child_directory)
        folders = []
        files = []
        for element in all_files_folders:
            if os.path.isfile(os.path.join(self.child_directory, element)):
                files.append(element)
            else:
                folders.append(element)
        if len(folders+files) == 0:
            return "Empty directory"
        out = ""
        if len(folders) > 0:
            out += "-"*70 + "\n"
            out += "|" + "Folders".center(68, " ") + "|" + "\n"
            out += "-"*70 + "\n"
            out += "| Name".ljust(30, " ") + "| " + "Size".ljust(8, " ") + \
                "| " + "Time of creation".ljust(27, " ") + "|" + "\n"
            for element in folders:
                stats = os.stat(os.path.join(self.child_directory, element))
                time = str(datetime.datetime.fromtimestamp(stats.st_ctime))
                size = str(stats.st_size)
                out += "| " + element.ljust(28, " ") + "| " + size.ljust(
                    8, " ") + "| " + time.ljust(27, " ") + "|" + "\n"
            out += "-"*70 + "\n"
        if len(files) > 0:
            out += "-"*70 + "\n"
            out += "|" + "Files".center(68, " ") + "|" + "\n"
            out += "-"*70 + "\n"
            out += "| Name".ljust(30, " ") + "| " + "Size".ljust(8, " ") + \
                "| " + "Time of creation".ljust(27, " ") + "|" + "\n"
            for element in files:
                stats = os.stat(os.path.join(self.child_directory, element))
                time = str(datetime.datetime.fromtimestamp(stats.st_ctime))
                size = str(stats.st_size)
                out += "| " + element.ljust(28, " ") + "| " + size.ljust(
                    8, " ") + "| " + time.ljust(27, " ") + "|" + "\n"
            out += "-"*70 + "\n"
        return out

    def create_folder(self, folder):
        """
            Create a new folder

            Parameters -
            ---------------------------
            folder - String of folder

            Returns -
            ---------------------------
            Response
        """
        if self.username is None:
            return "Login Please."
        if r"/" in folder or "\\" in folder:
            return "Don't add slashes in folder name."
        try:
            os.mkdir(os.path.join(self.child_directory, folder))
            return "Folder created with name %s" % folder
        except FileExistsError:
            return "Destination already contains folder with name %s" % folder

    def change_folder(self, folder):
        """
            Change directory

            Parameters -
            ---------------------------
            folder - String of folder

            Returns -
            ---------------------------
            Response
        """
        if self.username is None:
            return "Login Please."
        if not os.path.exists(os.path.join(self.child_directory, folder)):
            return "Destination folder doesn't exists."
        if self.allowed_folder(self.username, self.child_directory, folder):
            self.child_directory = os.path.join(self.child_directory, folder)
            return "Changed folder to %s" % self.get_path(self.child_directory)
        return "Permission Denied."

    def delete(self, username, password):
        """
            Delete a user

            Parameters -
            ---------------------------
            username - String of username

            password - String of password

            Returns -
            ---------------------------
            Response
        """
        if self.username is None:
            return "Login Please."
        with open(os.path.join(SERVER_DATABASE, 'login'), 'r') as data:
            content = data.read()
        content = content.lstrip("\n").rstrip("\n")
        users = content.split("\n")
        users = [user.split(",") for user in users]
        for user in users:
            if username == user[0]:
                if password == self.password:
                    self.delete_user(username)
                    return "Delete user."
                return "Wrong password"
        return "Username not found."
