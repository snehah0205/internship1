class Passenger:
    def __init__(self,name,passport_num,password):
        self.name=name
        self._passport_num=passport_num
        self.__password=password

    def display_detail(self):
        print("Name:",self.name)
        print("Passport Number:",self._passport_num)
        print("password:",self.__password)

    def password(self):
        return self.__password

   # def set_password(self, new_password):
     #   self.__password = new_password

passenger=Passenger("sneha","2345667","shashu25")
print("Name (public):",passenger.name)
print("Passport Number (protected):",passenger._passport_num)
print("Password (Privets):", passenger.password())

#passenger.set_password("teju")
passenger.display_detail()