class Location:
    def __init__(self, loc1, loc2):
        self.loc1 = loc1
        self.loc2 = loc2

    def __add__(self, other):
        return Location(self.loc1 + other.loc1, self.loc2 + other.loc2)

    def __truediv__(self, other):
        if other.loc1 == 0 and other.loc2 == 0:
            raise ValueError("Division by zero is not allowed")
        return Location((self.loc1 + other.loc1), (self.loc2 + other.loc2),(self.loc3 / other.loc3))

l1 = Location(23432, 33448)
l2 = Location(23445, 90087)
l3 = Location(84978, 98788)

Location_sum = l1 + l2 / 2

if location_sum.loc1 == l3.loc1 and location_sum.loc2 == l3.loc2:
    print(f"{l1.loc1} and {l2.loc2} are nearer to the location {l3.loc1}")
else:
    print(f"{l3.loc1} is not found")

    