# PYTHON CHEATSHEET

#0 NOTE :- DATA TYPES

#1 NOTE :- CREATING VARIABLES
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
# print(div(2, 50))
# print(div(5, 0))


