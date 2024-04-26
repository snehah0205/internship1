from py5 import AbstractFlowers

class Rose (AbstractFlowers):
    def display_details(self):
        print("Rose Detail")
        print("color:",self.color)
        print("number of petals:",self.num_petals)

class Jasmine (AbstractFlowers):
    def display_details(self):
        print("Jasmine Details")
        print("color:", self.color)
        print("number of petals:",self.num_petals)

class Lily (AbstractFlowers):
        def display_details(self):
            print("Lily Details")
            print("color:", self.color)
            print("number of petals:", self.num_petals)

class Sunflower (AbstractFlowers):
        def display_details(self):
            print("Sunflower Details")
            print("color:", self.color)
            print("number of petals:", self.num_petals)

class Marygold (AbstractFlowers):
        def display_details(self):
            print("Marygold Details")
            print("color:", self.color)
            print("number of petals:", self.num_petals)

