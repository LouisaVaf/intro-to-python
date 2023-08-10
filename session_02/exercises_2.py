# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
width = 10
height = 10
area = width * height
print("Rectagle of width " + str(width) + " and height " + str(height) + " has an area of " + str(area) +".")


# 2. Write code that prints the length of the string, 'python'.
print(len("python"))


# 3. Print out the first and third letter of the word 'python'.
print("python"[0])
print("python"[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name = input("Enter your name: ")
print("Hello " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = int(input("Enter your age: "))
age_in_15_years = age + 15
print("Your age in 15 years will be " + str(age_in_15_years))

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
print("Hello " + name + ", you are currently " + str(age) + " years old.\nIn 15 years time you will be " + str(age_in_15_years) + ".")


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input("Enter your hometown: ")
print(hometown.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
colour = input("What's your favourite colour? ")
print(len(colour))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
weather = input("What's the weather like? ")
month = input("Which month is it? ")
print("It is " + month + " and it is " + weather + " today.")


# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
t1 = int(input("Enter the temperature on Monday: "))
t2 = int(input("Enter the temperature on Tuesday: "))
t3 = int(input("Enter the temperature on Wednesday: "))
t4 = int(input("Enter the temperature on Thursday: "))
t5 = int(input("Enter the temperature on Friday: "))
average_t = (t1 + t2 + t3 + t4 + t5) / 5
print("It is " + month + " and the average temperature is " + str(average_t) + " degrees celsius.")

# 11. Print out the above sentence but make the month upper case.
print("It is " + month.upper() + " and the average temperature is " + str(average_t) + " degrees celsius.")


# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
favourite_animals = "\tDogs\n\tHamsters\n\tHorses\n\tOtters"
print(favourite_animals)


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
name2 = input("What's your name? ")
number = int(input("Pick any number between 0 and 5: "))
print(name2[number].upper())


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
print("WelcometoPython"[1:14:2])