class User:
    def __init__(self,username,password="1234"):
        self._username=username
        self.__password=password

    def check_password(self,password):
        return self.__password == password

    def change_password(self,new_password):
        self._password=new_password
        print("Password changed succesfully")

    def get_username(self):
        return self._username

username=input("enter ur username:")
user=User(username)
password =input("enter ur password:")

if user.check_password(password):
    print("welcome,{}!".format(user.get_username()))
else:
    print("password incorrect")
    change_option=input("do u want change ur password? (yes/no): ").lower()
    if change_option=="yes":
        new_password=input("enter ur new password:")
        user.change_password(new_password)
    else:
        print("gudby")