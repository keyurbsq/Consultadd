class Person:
    age1 = 0

    def __init__(self, age):
        if age < 0:
            print("Age is not valid, setting it to 0")
            self.age1 = 0
        else:
            self.age1 = age

    def amIOld(self):
        # num = Person(0)

        if 0 < self.age1 < 13:
            print("you are young")
        elif 13 <= self.age1 <= 19:
            print("you are teenage")
        elif self.age1 > 19:
            print("You are old")

    def yearPasses(self):
        self.age1 += 1
        print(self.age1)


a = Person(19)
a.amIOld()
a.yearPasses()