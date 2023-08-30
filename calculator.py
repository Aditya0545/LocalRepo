a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
operator = str(input("+, -, *, /: "))
if (operator == '+'):
    print("sum:",a+b)
elif (operator == '-'):
    print("Difference:",a-b)
elif (operator == '*'):
    print("Product:",a*b)
elif (operator == '/'):
    print("Divide:",a/b)
else:
    print("Invalid Input")