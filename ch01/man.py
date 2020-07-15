# -*- coding:utf-8 -*-

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Goodbye " + self.name + "!")


man = Man("David")
man.hello()
man.goodbye()
