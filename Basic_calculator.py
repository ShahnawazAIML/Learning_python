userFirstNumber = int(input("Write your first number here: "))
userSecondNumber = int(input("Write your second number here: "))
userOperation = input("Write the operation you want to do (e.g. '+','-','*','/'): ")

if userOperation == "+":
    print(userFirstNumber + userSecondNumber)
elif userOperation == "-":
    print(userFirstNumber - userSecondNumber)
elif userOperation == "*":
    print(userFirstNumber * userSecondNumber)
elif userOperation == "/":
    print(userFirstNumber / userSecondNumber)
else:
    print("Invalid operation!")
