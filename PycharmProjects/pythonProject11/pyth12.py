class Loction:
    def __init__(self,loction1,loction2):
        self.loction1 = loction1
        self.loction2 = loction2

    def __add__(self,other):
       return f"{self.loction1+other.loction1}+{self.loction2+self.loction2}i"

l1=Loction("23432","33448")
l2=Loction("23445","90087")
l3=Loction("84978","98788")
Loction=Loction1+Loction2/2
print(Loction)

    def __eq__(self, other):
        if self.loction==other.loction3:
            return True
        else:
            return False

if loction==loction3:
    print(f"{l1.Loction1} and{l2.Loction2} are nearer to the loction")
else:
    print(f"{l3.Loction3} is not found")