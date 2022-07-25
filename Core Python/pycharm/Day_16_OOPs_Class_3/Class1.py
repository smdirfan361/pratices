# Inheritance:
#        1.Single Inheritance
#        2.Multi level Inheritance
#        1.Multiple Inheritance


class car:
    def __init__(self, engin, tyre):
        self.body = "Steel"
        self.engine = engin
        self.tyre = tyre

    def milage(self):
        return


c = car( "v6", "radical")


class tata(car):
    pass


t = tata("Solid", "s4", "round")
if __name__ == "__main__":
    x = t.milage()
    print(type(x))
