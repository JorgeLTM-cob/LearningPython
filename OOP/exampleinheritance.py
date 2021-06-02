class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print (self.name,"has been created and he is",self.age,"years old.")

    def talk (self,*words):
        for phrase in words:
            print (self.name,':',phrase)


class Player(Person):
    
    def __init__(self, age, name, sport):
        self.age = age
        self.name = name
        self.sport = sport
        print (self.name,"has been created and he is",self.age,"years old.")
    
    def practice(self):
        print (self.name,":I am practicing")

juan = Person(30, "Juan")
juan.talk("Hello, I am talking.","This is me")
louis = Player(18, "Louis","swimming")
louis.talk("Hello, I am talking.","This is me")
louis.practice()
print ("Louis practices",louis.sport)


