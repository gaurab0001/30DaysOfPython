#day 28 of 30 days python challenge 
#Topic - Access Specifires in python

class Student:
    def __init__ (self,name,marks,password):
        self.name= name 
        self._marks=marks
        self.__password=password

    def display_public(self):
            print("name(public):",self.name)

    def display_protected(self):    
            print("marks(protected):",self._marks)

    def display_private(self):    
            print("password(private):",self.__password)

s= Student("gaurab",85,"gaurab123")           
s.display_public()
s.display_protected()
s.display_private()