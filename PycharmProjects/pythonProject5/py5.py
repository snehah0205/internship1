from abc import ABC ,abstractmethod

class AbstractFlowers(ABC):
    def __init__(self,color,num_petals):
        self.color=color
        self.num_petals=num_petals

    @abstractmethod
    def display_details(self):
        pass