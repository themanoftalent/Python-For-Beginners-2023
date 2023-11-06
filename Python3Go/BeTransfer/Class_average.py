students=int(input('Please enter the number of students in the class: '))
class_average = 0
maximum_num = 0
minimum_num = 100
for number in range(students):

  first_grade=int(input("Enter student's first grade: "))
  second_grade=int(input("Enter student's second grade: "))
  third_grade=int(input("Enter student's third grade: "))

  StudentAverage=(first_grade + second_grade + third_grade)/3
  print("The student's average is", round(StudentAverage,2))

  class_average= class_average + StudentAverage
  print("The class average is", round(class_average/(number+1),2))

  if StudentAverage > maximum_num:
    maximum_num = StudentAverage

  if StudentAverage < minimum_num:
    minimum_num = StudentAverage
print("The minimum average is", round(minimum_num,2))
print("The maxiumum average is", round(maximum_num,2))
