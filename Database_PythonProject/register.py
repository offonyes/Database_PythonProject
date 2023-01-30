class System():
    def __init__(self):
        with open("database.txt", "a+") as file:
            pass
        with open("notes.txt", "a+") as file:
            pass
        with open("database.txt", "r") as file:
            self.Accounts = len(file.readlines())
    
    def Access_Granted(self):
        print("********** Welcome! **********")
        print("******** USER DETAILS ********")
        print("------------------------------")
        print("|"+"Username: "+'{:>18}'.format(name)+"|")
        print("------------------------------")
        print("**********USER NOTES**********")
        print("------------------------------")
        with open("notes.txt","r") as file:
            for dates in file:
                saved_names,saved_notes = dates.split("&/!")
                saved_notes = saved_notes.strip()
                if saved_names==name:
                    print(saved_notes)         
        choice2 = (input("You can choose: logout, change password or change notes\n")).lower()
        if choice2 =="logout":
            self.Begin()
        elif choice2 =="change password":
            self.Change_Password()
        elif choice2 == "change notes":
            self.Change_Note()
        else:
            self.Access_Granted()

    def Change_Note(self):
        new_notes = ""
        adding_rewriting = (input("Choose 'add','clear' your notes or 'return' to profile.\n")).lower()
        if "add" in adding_rewriting:
            newnotes = str(input("Write new notes.\n"))
            with open("notes.txt","r") as file:
                for dates in file:
                    saved_names,saved_notes = dates.split("&/!")
                    saved_notes = saved_notes.strip()
                    if saved_names==name:
                        if saved_notes == "Write notes":
                            saved_notes = ""
                        saved_notes += newnotes 
                    new_notes += saved_names + "&/!" + saved_notes + "\n"      
        elif "clear" in adding_rewriting:
            with open("notes.txt","r") as file:
                for dates in file:
                    saved_names,saved_notes = dates.split("&/!")
                    saved_notes = saved_notes.strip()
                    if saved_names==name:
                        saved_notes = "Write notes"
                    new_notes += saved_names + "&/!" + saved_notes + "\n"
        elif "return" in adding_rewriting:
            self.Access_Granted()
        else:
            self.Change_Note()
        change_file = open("notes.txt", "w")
        change_file.write(new_notes)
        change_file.close()      
        self.Change_Note()
    def Login(self):
        global name
        success = False
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        with open("database.txt","r") as file:
            for dates in file:
                saved_names,saved_passwords = dates.split(",")
                saved_passwords = saved_passwords.strip()
                if saved_names==name and saved_passwords==password:
                    success = True
        if(success):
            print("Login Successful")
            self.Access_Granted()
        else:
            print("Wrong user name or password")
            self.Login()

    def Registration(self):
        global name
        name_in_list = False
        name = input("Enter your name and password to register.\nEnter your name: ")
        password = input("Enter your password: ")
        with open("database.txt", "r") as file:
            for dates in file:
                saved_names,saved_passwords = dates.split(",")
                if saved_names==name:
                    name_in_list = True
        if name_in_list == True :
            print("This Name is used")
            self.Begin()
        else:
            with open("database.txt", "a") as file:
                file.write(name+","+password+"\n")
            with open("notes.txt","a") as file:
                file.write(name + "&/!Write notes\n")
            self.Accounts +=1
            self.Access_Granted()

    def Change_Password(self):
        new_database = ""
        password = str(input("For changind password input.\nOld Password: "))
        newpassword = str(input("New Password: "))
        with open("database.txt","r") as file:
            for dates in file:
                saved_names,saved_passwords = dates.split(",")
                saved_passwords = saved_passwords.strip()
                if saved_names==name and saved_passwords==password:
                    saved_passwords = saved_passwords.replace(password,newpassword)
                new_database += saved_names + "," + saved_passwords + "\n"
        change_file = open("database.txt", "w")
        change_file.write(new_database)
        change_file.close()
        user_input = ""
        while user_input != "return":
            user_input = (input("You successfuly changed password.\nYou can 'return' to your profile: ")).lower()
            if user_input == "return":
                self.Access_Granted()
                break
            else:
                print("Write only 'return'")

    def Begin(self):
        choice = (input("Login or Register: ")).lower()
        if choice =="login" and self.Accounts > 0:
            self.Login()
        elif choice =="register":
            self.Registration()
        else:
            self.Begin()

mySystem = System()
mySystem.Begin()