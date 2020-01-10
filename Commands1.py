    def create_folder(self, path):
        """
            For creating a new folder of specified name.

            Return : str
                message to the client.
        """
        root_directory = os.path.join("data", self.user_name, self.current_directory)
        active_directories = []
        if not self.login:
            return "\nCan you login first?"
        for sub in os.listdir(root_directory):
            if os.path.isdir(os.path.join(root_directory, sub)):
                active_directories.append(sub)
        if path in active_directories:
            return "\nDirectory Already Present"
        os.mkdir(os.path.join(root_directory, path))
        return "\nSuccess."

    def read_write(self, path, total_files):
        """"
            Function to access both read and write functions.
        """

        if not self.login:
            return "\nCan you login first?"
        for file in os.listdir(os.path.join("data", self.user_name, self.current_directory)):
            if os.path.isfile(os.path.join("data", self.user_name, self.current_directory, file)):
                total_files.append(file)

    def reset_read_file(self):
        """
            Used to reset the saved read index for the files.

            Return : str
                Message to the client.
        """
        if not self.login:
            return "\nCan you login first?"
        for path in list(self.index_read.keys()):
            self.index_read[path] = 0
        return "\nReset the index of all read_file."

    def read_file(self, path):
        """
            Returns the data of specified file.

            Return : str
                Message to the client.
        """
        total_files = []
        self.read_write(path, total_files)
        if path not in total_files:
            return "\nFile not found."
        total_path = os.path.join("data", self.user_name, self.current_directory, path)
        if total_path not in list(self.index_read.keys()):
            self.index_read[total_path] = 0
        with open(total_path, "r") as file:
            contents = file.read()
        old_index = str(self.index_read[total_path]*self.char_num)
        index = self.index_read[total_path]
        data = contents[index*self.char_num:(index+1)*self.char_num]
        self.index_read[total_path] += 1
        self.index_read[total_path] %= len(contents)//self.char_num + 1
        return "\n" + "Command - read_file from " + old_index + " to " + str(int(old_index)+self.char_num) + " are - \n" + data

    def write_file(self, path, write_data):
        """
            Writes data to desired directory.
            If the file is not present, then a new file will be created.

            Return : str
                Message to the client.
        """
        total_files = []
        self.read_write(path, total_files)
        total_path = os.path.join("data", self.user_name, self.current_directory, path)
        if path in total_files:
            with open(total_path, "a+") as file:
                write_data = "\n" + write_data
                file.write(write_data)
            return "\nSuccess."
        with open(total_path, "w+") as file:
            file.write(write_data)
        return "\nSuccess."
