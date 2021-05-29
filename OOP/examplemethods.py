class Person:
    def __init__(self):
        self.age = 18
        self.name = "Juan"
        print (self.name,"has been created and he is",self.age,"years old.")

    def talk (self, word = "I don't know what I should say."):
        print (self.name,':',word)

juan = Person()
juan.talk()
juan.talk("Hello, I am talking.")

