''' Create a simple student record system using classes and objects. Define a student class to represent students and their information

use attributes
1.Name
2.Roll No.
3.Marks         '''
# Name : Aditya Kumar
#ID : 22BTCSE067

class students():
    def info(self):
        print(f"Name : {self.name_of_student}\nRoll no. {self.Roll}\nMarks : {self.marks_of_student}")

student1 = students()
student1.name_of_student = "Aditya Kumar"
student1.Roll = 67
student1.marks_of_student = 70

student2 = students()
student2.name_of_student = "Noor Ali"
student2.Roll = 64
student2.marks_of_student = 80

student3 = students()
student3.name_of_student = "Muskan Kumari"
student3.Roll = 79
student3.marks_of_student = 75

student4 = students()
student4.name_of_student = "Arshita Navin"
student4.Roll = 120
student4.marks_of_student = 85

student1.info()
print("\n")
student2.info()
print("\n")
student3.info()
print("\n")
student4.info()

