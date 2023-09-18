def avg_grade():
    marks1 = float(input("Enter Your 1st Marks: "))
    marks2 = float(input("Enter Your 2nd Marks: "))
    marks3 = float(input("Enter Your 3rd Marks: "))
    marks4 = float(input("Enter Your 4th Marks: "))
    marks5 = float(input("Enter Your 5th Marks: "))
    solve = (marks1+marks2+marks3+marks4+marks5) / 5
    print("{} is the Average Grade".format(solve))

avg_grade()