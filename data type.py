# Datatype

number = 60  # integer{ int}
num = 34.77  # decimal{ float}

Greeting = "hello there"  # string{text}
Ispythoninteresting = True  # bool

# A variable with multiple values

languages = ["python", " PHP", "java",
             "kotlin"]  # this is a list which is numbered from element no 0. It uses special brackets.
print(languages)

Fruits = (
    "apple", " banana", "pear")  # this is a tuple . it uses normal brackets. you can never change an element in a tuple
print(Fruits)

Countries = {"Kenya", " Ghana", "Sweden", "Turkey",
             "Egypt"}  # This is a set. they dont follow any order.  they use  calibraces they are also unchangeable

# Dictionary. it has a key and a value... uses calibraces
Details = {
    "Firstname": " Ashley",
    "Course": "MIT",
    "age": 18,
    "Nationality": "US"
}
# ie
employee = {
    "Chairman": "Cahlmer",
    "Secretary": "Halima",
    "Partner": "Jacobs",
}
print(employee["Secretary"])
print(num)
print(number)
print(Greeting)
print(Ispythoninteresting)
print(Countries)
# calling individual variables in a given dictionary
print(Details["Firstname"])
print(Details["Nationality"])
print(Details["age"])
print(employee["Chairman"])
# Determining the data typeof a variable... either set, dictionary,tuple,list..
print(type(Details))
print(type(Countries))
print(type(Greeting))

# Typecasting.... process of converting one data from one type to another ie decimal to whole
print(float(number))  # converting whole no to decimal
print(int(num))  # converting  decimal to whole no

# ie
x = 34567.0876
y = 87654
print(int(x))
print(float(y))

# list
Players = ["messi", "ronaldo", "neymar", "davido"]

# tuple
airlines = ("jkia", "mombasa", "amboseli", "laikipia")

# set
car = {"Mansory", "Cullinan", "Pagani", "Benjamina", "Benz"}

# dictionary
moviestars = {

    "IP man": "Donnie Yen",
    "The Rock": "Dwayne Johnson",
    "Thomas Shelby": "Cilian Murphy",
    "Commando": "Michael Jai White"
}

a = 345.145
b = 23456543

print(a + b)
print(int(a))
print(float(b))

print(car)
print(type(car))

print(Players)
print(type(Players))
print(Players[3])
print(Players[2])

print(Players)
print(type(Players))

print(moviestars)
print(moviestars["Commando"])
print(moviestars["The Rock"])
print(moviestars["IP man"])
