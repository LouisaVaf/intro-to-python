# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
name = input("What is your name? ")
if name == "Bob":
  print("Welcome Bob!")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
name = input("What is your name? ")
if name != "Alice":
  print("You're not Alice!")
  

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
password = input("Please enter password. ")
if password == "qwerty123":
  print("You have successfully logged in")
else:
  print("Password failure" )

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
number = int(input("Please enter a number: "))
if number % 2 == 0:
  print("Even")
else:
  print("Odd")
  

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
total = number1 + number2
if total > 21:
  print("Bust")
else:
  print("Safe")
  

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
length = input("Enter a length: ")
width = input("Enter a width: ")
if length == width:
  print("This shape is a square. ")
else:
  print("This shape is not a square. ")
  

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("What is your current salary? "))
yearsofservice = int(input("How many years have you worked for our company? "))
bonus = 0.1 * salary
if yearsofservice >= 3:
  print("For a salary of " + str(salary) + ", you will receive a bonus of " + str(bonus) + "." )
else:
  print("No bonus.")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
wholenumber = int(input("Enter a whole number: "))
if wholenumber >= 0:
  print(wholenumber**3)
else:
  print(wholenumber/2)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
altname = input("What is your name? ")
if altname == "Alice":
  print("Hello Alice.")
elif altname == "Bob":
  print("You're not Bob! I'm Bob.")
else:
  print("You must be Charlie.")


# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
age = int(input("Please enter your age: "))
if age < 11:
  print("You're too young to go to this school.")
elif age > 11 and age < 16:
  print("You can come to this school.")
elif age > 16:
  print("You're too old for school.")
elif age == 0:
  print("You're not born yet!")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
month = input("Enter the name of a month: ")
if month == "March" or "April" or "May":
  print(month + " is in Spring.")
elif month == "June" or "July" or "August":
  print(month + " is in Summer.")
elif month == "September" or "October" or "November":
  print(month + " is in Autumn.")
elif month == "December" or "January" or "February":
  print(month + " is in Winter.")
else:
  print("I don't know.")



# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
  print("Even")
elif num1 % 2 != 1 and num2 % 2 != 0:
  print("Odd")
else:
  print(num1 + num2)


# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))
if n1 > n2:
  print(n1)
elif n2 > n1:
  print(n2)
else:
  print("Both numbers are equal.")


# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("What is your current salary? "))
yearsofservice = int(input("How many years have you worked for our company? "))
if yearsofservice > 7:
  print("For a salary of " + str(salary) + ", you will receive a bonus of " + str(0.2 * salary) + "." )
elif yearsofservice > 5:
  print("For a salary of " + str(salary) + ", you will receive a bonus of " + str(0.15 * salary) + "." )
elif yearsofservice >= 3 and yearsofservice <= 5:
  print("For a salary of " + str(salary) + ", you will receive a bonus of " + str(0.1 * salary) + "." )
else:
  print("No bonus")


# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
name1 = input("Enter the name of person one: ")
name2 = input("Enter the name of person two: ")
name3 = input("Enter the name of person three: ")
age1 = int(input("Enter the age of person one: "))
age2 = int(input("Enter the age of person two: "))
age3 = int(input("Enter the age of person three: "))
if age1 > age2 and age1 > age2:
  print(name1 + " of age " + str(age1) + " is the oldest.")
elif age2 > age1 and age2 > age3:
  print(name2 + " of age " + str(age2) + " is the oldest.")
elif age3 > age1 and age3 > age2:
  print(name3 + " of age " + str(age3) + " is the oldest.")
else:
  print("You are all the same age.")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson1 = input("Please enter your lesson name: ")
mark1 = int(input("Pleasze enter you mark for this lesson: "))

if mark1 >= 80:
  print("Your grade is A for " + lesson1)
elif mark1 >= 60 and mark1 < 80:
  print("Your grade is B for " + lesson1)
elif mark1 >= 50 and mark1 < 60:
  print("Your grade is C for " + lesson1)
elif mark1 >= 45 and mark1 < 50:
  print("Your grade is D for " + lesson1)
elif mark1 >= 25 and mark1 < 45:
  print("Your grade is E for " + lesson1)
elif mark1 <2:
  print("Your grade is F for " + lesson1)