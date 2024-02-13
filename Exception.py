# exceptions and how to deal with them
# exception Handling ... these are errors

# try enables you to remove your error instead of displaying the error replacing it with what is in the except.....
# finally displays the text whether the 
try:
    print(x)

except:
    print("Benny hinn")
finally:
    print("Success")
num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("An error occurred")



    # user defined functions
try:
    def multiply(number1, number2):
        return number1 * number2
except:
    print("An error occurred")
finally:
    print("Success")
print(multiply(6, 4))
