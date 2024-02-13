temperature = 32
if temperature > 37:
    print("It Is Hot")
else:
    print("It Is Cold")
    # A program that prints the largest among three numbers
num1 = 45
num2 = 89
num3 = 32
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, " is the largest number")
else:
    print(num3, " is the largest number")

# smallest number
num1 = 45
num2 = 89
num3 = 32
if num1 < num2 and num1 < num3:
    print(num1, "is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2, "is the smallest number")
else:
    print(num3, " is the smallest number")

    # A program that checks whether a number is even or odd
number = 56
if number % 2 == 0:
    print(number, " is even")
else:
    print(number, "is odd")


#  A program investigating if a number is a prime  or not
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Test the function
num = 23
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


# program (individual ...)
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

        return True


# testing the function myself....


number = 14
if is_prime(number):
    print(number, "is a prime number"),
else:
    print(number, "is not a prime number")

