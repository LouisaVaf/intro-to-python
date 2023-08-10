# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
#import random
#for number in range(10):
#    print(random.randint(1, 100))


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
#import random
#computer_choice = random.randint(1,10)
#user_choice = None
#while user_choice != computer_choice:
#  user_choice = int(input("Guess the computers number: "))
#print("You guessed the computers number!")


# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
#import math  
#width = None
#length = None
#user_width = int(input("Enter a width in cm: "))
#user_length = int(input("Enter a length in cm: "))
#print(str(math.ceil((user_width * user_length) * (10**(-2)))))


# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
#user_input = input("Please enter your password: ")
#password = "qwerty123"
#user_guesses = 0

#while user_guesses < 2:
 # if user_input == password:
  #  print("You have successfully logged in")
   # break
  #else:
   # print("Password failure")
    #user_input = input("Please enter your password: ")
    #user_guesses += 1
#if user_guesses == 2:
 # print("System Locked!")
  


# 5. Add up all the numbers from 1 to 500 and print the answer.
#total = 0
#for x in range(1, 501):
#  total += x
#print(total)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
#list = []
#numbers = ""
#number_list = 0
#x = 0
#print("Pick 10 numbers, one of which must be 99.")

#while number_list <= 10:
 # numbers = int(input("Pick a number: "))
  #list.append(numbers)
  #number_list += 1

#while x < len(list):
 # if list[x] == 99:
  #  print("The number 99 is at index " + str(x))
   # x += 1



# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
#number = 0
#while number < 16:
#  print(number*18)
#  number += 1
  


# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
#number = 0
#while number < 101:
#  print(number)
#  number += 1


# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
import random
prize_draw = []
user_input = None

for name in range(5):
  name = input("Enter a name: ")
  prize_draw.append(name)

print(random.choice(prize_draw))


# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
