class Party:
    def __init__(self,name,money):
        self.name=name
        self.money=money

    def __gt__(self,other):
        if self.money>other.money:
            return True
        else:
            return False

p1=Party("Sneha",499478)
p2=Party("vaish",766879)

if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")
