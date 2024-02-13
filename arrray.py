# constructing an array

courses = ["MIT", "CyberSecurity", "DataScience" ]
print(courses)

# accessing an element in an array
print(courses[1])  # this shows index position 1

# looping through an array ...

# A for loop...
for course in courses:
    print(course)

# adding an element  in an array... use append
courses.append("Android Development")
print(courses)

# Deleting an element in an array.
courses.remove("CyberSecurity")
print(courses)
