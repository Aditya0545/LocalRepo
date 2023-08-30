# Programming to print grade according to score
score = float(input("Enter Your Marks: "))
if (score >= 90) and (score <= 100):
    print("Grade A")
elif (score >= 75) and (score <= 89.99):
    print("Grade B")
elif (score >= 60) and (score <= 74.99):
    print("Grade C")
elif (score >= 40) and (score <= 59.99):
    print("Grade D")
else:
    print("Fail")
