# PYTHON CHEATSHEET

#0 NOTE :- DATA TYPES

#1 NOTE :- CREATING VARIABLES
#from _typeshed import Self


name = "Prince Kyeremanteng Samuel"     # string variable
age = 23                                # int variable
gpa = 3.46                              # floating point variable
married = False                         # boolean variable
friends = ["John", "Jane", "Jack"]      # List
agesOfFriends = {"John":21, "Jane":20, "Jack":22}   # dictionary
hobbies = {"Coding", "Music", "Movie"}              # set
ranges = range(1, 20)                               # range

#2 NOTE :- OUTPUTTING VALUES
# print("Hello world")
# print(age)
# print(ranges)
# print(f"LIST OF MY FRIENDS: {friends}")

#3 NOTE :- INPUTING VALUES
# newName = input("Enter new name: ")
# age = input("Enter age: ")

#4 NOTE :- TYPE CASTING
age = int("24")
trueOrFalse = bool(0)
givenBirth = bool(1)
asciiCode = ord("g")
setToList = list({1, 2, 3, 4, 5})
listToSet = set([10, 20, 25, 30, 35])
nestedListToDic = dict([["name", "Prince"], ["age",23], ["town","Amanfrom"]])

print(nestedListToDic)

#5 NOTE :-  FUNCTIONS - NO RETURN STATEMENT
def sayHi():
    print("Hi")



def greet(name):
    print(f"Hello {name}")


def add(a, b):
    print(a + b)

def mult(a, b):
    print(a * b)

# FUNCTIONS WITH RETURN STATEMENT
def sayHi2():
    return "Hi"

def greet2(name):
    return f"Hello {name}"

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    if(b != 0):
        return a / b
    else:
        return "Zero division error"

class Bird:
    '''A class prototype || Create birds'''
    def __init__(self, name, age, legs):
        '''Init method sets the name and age of the bird'''
        self.name = name
        self.age = age
        self.legs = legs

    def setName(self, newName):
        '''Gives the bird  new name'''
        self.name = newName

    def setAge(self, newAge):
        '''Give the bird a new age'''
        self.age = newAge


    def getName(self):
        '''Gets the names of the current bird'''
        return self.name
    
    def getAge(self):
        '''Gets the age of the current bird'''
        return self.age

#creates an instance of the bird class  | birdOne becomes an instance (object of the Bird class)
birdOne = Bird("Birdy", 2, 2)

birdOne.setAge(5)
birdOne.setName("Buddy")
print(birdOne.getAge())
print(birdOne.getName())
