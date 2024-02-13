# While loop
# Incremeting a value
number = 5
while number <= 10:
    print(number)
    number += 1

    # Decrementing values
number = 105
while number >= 99:
    print(number)
    number -= 1

# using break... - it causes a program to stop  printing
# continue - ignores a given number..


# BREAK statement
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 2

# CONTINUE statement
y = 19
while y <= 25:
    y += 1
    if y == 23:
        continue
        print(y)

# for loop

languages = ["python", "java", "ruby", "c++", "c", "c"]
for lang in languages:
    print(lang)

    # printing a range of values
# Range
for z in range(6):
    print(z)
# range of 20 to 30 hence use the number above where you want to reach
for a in range(20, 31):
    print(a)

for b in range(30, 41, 2):
    print(b)

word = "innovation"
for word in "innovation":
    print(word)


for letter in "assembly":
    print(letter)
