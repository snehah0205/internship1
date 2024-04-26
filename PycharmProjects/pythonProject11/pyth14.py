class Location:
    def __init__(self, loc1, loc2):
        self.loc1 = loc1
        self.loc2 = loc2

    def __add__(self, other):
        if self.loc1 == other.loc1 and self.loc2 == other.loc2:
            return f"{self.loc1} and {self.loc2} are near to the location3 {other.loc1}"
        else:
            return f"Location {other.loc1} is not found"

l1 = Location(23432, 33448)
l2 = Location(23445, 90087)
l3 = Location(23432, 33448)

result = l1 + l2
print(result)

result = l1 + l3
print(result)

    