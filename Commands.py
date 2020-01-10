 def user_reg(self, user, user_password, user_privileges):
        """
            For registering a new user.It saves data in server session.
            Return : str
                message to client.
        """
        if user in self.login_dict['user_name'].tolist():
            return "\nuser_name not available"
        if user == "" or user_password == "" or user_privileges == "":
            return "\nYou cannot register empty user"
        temp = pandas.DataFrame(columns=['user_name'])
        temp['password'] = user_password
        temp['user_name'] = [user]
        if user_privileges.lower() == 'admin':
            temp['isAdmin'] = 1
        else:
            temp['isAdmin'] = 0
        self.login_dict = self.login_dict.append(temp)
        self.login_dict.to_csv("serverSession/users.csv", index=False)
        self.login_dict = pandas.read_csv("serverSession/users.csv")
        self.active_users = pandas.read_csv("serverSession/loginUsers.csv")
        os.mkdir(os.path.join("data", user))
        return "\nRegistered user successfully."

    def user_login(self, user, password):
        """
            For user login
            Return : str
                message to client.
        """

        self.login_dict = pandas.read_csv("serverSession/users.csv")
        self.active_users = pandas.read_csv("serverSession/loginUsers.csv")
        if self.login:
            return "\nAlready logged in"
        if user not in self.login_dict['user_name'].tolist():
            return "\nuser_name not registered"
        if password != str(self.login_dict.loc[self.login_dict['user_name'] == user, 'password'].iloc[0]):
            return "\nWrong password!"
        if user in self.active_users['user_name'].tolist():
            return "\nLogged in from different IP"
        self.login = True
        self.user_name = user
        self.current_directory = ""
        temp = pandas.DataFrame(columns=['user_name'])
        temp['user_name'] = [user]
        self.active_users = self.active_users.append(temp)
        self.active_users.to_csv("serverSession/loginUsers.csv", index=False)
        return "\nLogin completed."

    def change_folder(self, root_directory):
        """
            Changes folder to desired folder required by the user.
            Return : str
                message to the client.
        """
        total_list = []
        for direc, files, sub in os.walk(os.path.join("data", self.user_name)):
            total_list.append(os.path.normpath(os.path.realpath(direc)))
        if not self.login:
            return "\nCan you login first?"
        path_to_be_change = os.path.join("data", self.user_name, self.current_directory, root_directory)
        path_to_be_change = os.path.normpath(os.path.realpath(path_to_be_change))
        if path_to_be_change in total_list:
            self.current_directory = os.path.join(self.current_directory, root_directory)
            return "\nChanged directory to " + root_directory + " successfully"
        return "\nWrong directory name."

    def list(self):
        """
            Gives information about the list of files and folder for user .
            Return : str
               message to the client. 
        """
        list_of_files = []
        for i in os.listdir(os.path.join("data", self.user_name, self.current_directory)):
            a = os.stat(os.path.join(os.path.join("data", self.user_name, self.current_directory), i))
            list_of_files.append([i, str(a.st_size), str(time.ctime(a.st_ctime))])
        if not self.login:
            return "\nCan you login first?"
        response = "\nFile | Size | Date modified\n"
        for data in list_of_files:
            new_line = " | ".join([data[0], data[1], data[2]]) + "\n"
            response += "~~~~~~\n" + new_line
        return response
