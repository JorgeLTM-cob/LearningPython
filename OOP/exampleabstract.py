from abc import ABCMeta, abstractmethod

class Person:
    __metaclass__ = ABCMeta
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print (self.name,"has been created and he is",self.age,"years old.")

    @abstractmethod
    def talk (self,*words):  
        for phrase in words:
            print (self.name,':',phrase)
        pass

class Player(Person):
    
    def __init__(self, age, name, sport):
        self.age = age
        self.name = name
        self.__sport = sport
        print (self.name,"has been created and he is",self.age,"years old.")
    
    def practice(self):
        print (self.name,": I am practicing")

    def mySport(self):
        return self.__sport

    def talk(self, *words):
        for phrase in words:
            print (self.name, ':' , phrase)

#juan = Person(30, "Juan")
#juan.talk("Hello, I am talking.","This is me")
louis = Player(18, "Louis","swimming")
louis.talk("Hello, I am talking.","This is me")
louis.practice()
print ("Louis practices",louis.mySport())


