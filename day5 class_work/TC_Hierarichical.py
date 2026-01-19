class Theatre:
    def show(self):
        print("Theatre has movies")

class MorningShow(Theatre):
    def popcorn(self):
        print("Sweet popcorn")

class NoonShow(Theatre):
    def icecream(self):
        print("Choc icecream")

obj1=NoonShow()
obj1.show()
obj1.icecream()

obj2=MorningShow()
obj2.show()
obj2.popcorn()