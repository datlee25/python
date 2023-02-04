from Person import Person


class LeDat(Person):
    p1 = Person("Dat",123)
    print(p1.name)
    def __init__(self):
        print("a")
ledat = LeDat()

