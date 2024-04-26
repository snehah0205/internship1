n=int(input('enter the number of terms'))
count=0
while n!=0:
    n//=10
    count+=1
print(count)


///password
attempts=0
password="python"
while attempts<2:
    my_password = input("enter the password")
    if (my_password == password):
        print("password is correct, welcome")
    else:
        attempts+=1
        print("ur password is incorrect")
else:
    print("ur account has been blocked ,plz try again later")


//password
attempts=3
password="python"
while attempts>0:
    my_password = input("enter the password")
    if (my_password == password):
        print("password is correct, welcome")
        break
    else:
        attempts-=1
        if attempts>0:
            print(f"ur password is incorrect! you have {attempts} attempts left..")
        else:
            print("ur account has been blocked ,plz try again later")
            break


//student data
# Dummy student data stored in a dictionary
student_data = {
    "101": {"name": "Surya", "marks": 75},
    "102": {"name": "Anu", "marks": 50},
    "103": {"name": "Vipin", "marks": 90},
    "104": {"name": "Sara", "marks": 35},
    "105": {"name": "Santhosh", "marks": 80}
}

# Function to check if a user exists and print their details
def check_user(roll_number):
    if roll_number in student_data:
        student = student_data[roll_number]
        name = student["name"]
        marks = student["marks"]
        result = "Pass" if marks >= 50 else "Fail"
        print(f"Student Name: {name}")
        print(f"Roll Number: {roll_number}")
        print(f"Marks: {marks}")
        print(f"Result: {result}")
    else:
        print("Student not found!")

# Example usage
roll_number = input("Enter student's roll number: ")
check_user(roll_number)


//object oriented program
class Bike:
    pass
duke=Bike()
duke.name=("RC390")
duke.cc=390
print(duke.cc)

RE=Bike()
RE.name="classic350"
RE.CC=350
print(RE.name)



class Bike:
    def __init__(self,name,cc):
        self.bike_name=name
        self.bike_cc=cc

    def Sound(self):
        print(f"{self.bike_name} is loud")

Duke=Bike("RC390", 390)
RE=Bike("classic350",350)

print(Duke.bike_name)
print(RE.bike_name)
Duke.Sound()


class Animal:
    def __init__(self, name, color):
        self.animal_name = name
        self.animal_color = color


dog = Animal("tommy", "golden")
cat = Animal("lisa", "white")
lion = Animal("lionel", "orange")
snake = Animal("havuu", "black")
cow = Animal("laxmi", "brown")

print(dog.animal_name, dog.animal_color)
print(cat.animal_name, cat.animal_color)
print(lion.animal_name, lion.animal_color)
print(snake.animal_name, snake.animal_color)
print(cow.animal_name, cow.animal_color)



class Student:
    def __init__(self,name,rollno,marks):
        self.Student_name=name
        self.Student_rollno=rollno
        self.Student_marks=marks

st1=Student("vaish","22","907")
st2=Student("tej","73","834")
st3=Student("harshi",19,"7898")
st4=Student("sneha","49","654")

print(st1.Student_name , st1.Student_rollno)
print(st2.Student_name , st2.Student_rollno)
print(st3.Student_name , st3.Student_rollno)
print(st4.Student_name , st4.Student_rollno)





class Bike:
    def __init__(self,name,cc):
        self.bike_name=name
        self.bike_cc=cc

    def Type(self):
        if self.bike_cc<200:
            print(f"{self.bike_name} is normal bike")
        else:
            print(f"{self.bike_name} is superbike")

Duke=Bike("RC390", 390)
RE=Bike("classic350",350)
Hero=Bike("splendor",110)

b=input("enter the bike")
if b=="Duke":
    Duke.Type()
elif b=="RE":
    RE.Type()
else:
    Hero.Type()


    class Human:
        def __init__(self, hobby, food):
            self.fav_hobby = hobby
            self.fav_food = food

        def display_info(self):
            print(f"he plays{self.fav_hobby} and he likes{self.fav_food}")


class Human:
    def __init__(self,hobby,food):
        self.fav_hobby=hobby
        self.fav_food=food
    def display_info(self):
        print(f"she plays{self.fav_hobby} ,and she likes  {self.fav_food}")

class suki(Human):
    def __init__(self,hobby,food,language):
        super().__init__(hobby,food)
        self.fav_language=language

    def display_info(self):
        super().display_info()
        print(f"language she speaks{self.fav_language}")
user =suki("games","dose","korean")
user.display_info()