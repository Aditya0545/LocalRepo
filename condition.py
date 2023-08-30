# programming to check the input number is 0, +ve or -ve
num = int(input("Enter the number: "))
if num == 0:
    print("The number is zero")
elif num > 0:
    print("The number is +ve number")
elif num < 0:
    print("The number is -Ve number")
else:
    print("Invalid Input")