class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print (self.name,"has been created and he is",self.age,"years old.")

    def talk (self, word = "I don't know what I should say."):
        print (self.name,':',word)

juan = Person(18, "Juan")
louis = Person(20, "Louis")
juan.talk("Hello, I am talking.")
louis.talk("Hello, I am talking.")
