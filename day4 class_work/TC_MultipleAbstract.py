from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def interest(self):
        pass

class Union(Bank):
    def loan(self):
        print("loan is 30k")

    def interest(self):
        print("Interest is 2k")

u=Union()
u.loan()
u.interest()