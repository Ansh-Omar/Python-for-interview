# Program 83
'''
Define a class Person and its two child classes: Male and Female. All classes have a
method "getGender" which can print "Male" for Male class and "Female" for Female
class.'''

class Person():
    def getGender(self):
        print("Don,t know.")
class Male(Person):
    def getGender(self):
        print("Male")
class Female(Person):
    def getGender(self):
        print("Female")
        
Human = Person()
Ansh = Male()
Anshika = Female()

Human.getGender()
Ansh.getGender()
Anshika.getGender()