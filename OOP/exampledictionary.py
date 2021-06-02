class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print (self.name,"has been created and he is",self.age,"years old.")

    def talk (self,**words):
        for phrase in words:
            print (self.name,':',words[phrase])

juan = Person(30, "Juan")
juan.talk(t1 = "Hello, I am talking.",t2 = "This is me")
louis = Person(18, "Louis")
juan.talk(t1 = "Hello, I am talking.",t2 = "This is me")

