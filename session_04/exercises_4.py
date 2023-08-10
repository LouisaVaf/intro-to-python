# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
#fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
#print(fruit)


# 2. Add "Grapes" to the list and print the list.
#fruit.append("Grapes")
#print(fruit)


# 3. Change "Pears" to "Strawberries" and print the list.
#fruit[2] = "Strawberries"
#print(fruit)


# 4. Remove "Apples" from the list and print the list.
#del(fruit[0])
#print(fruit)


# 5. Print out the current length of the list.
#print(len(fruit))


# 6. Order the list alphabetically.
#fruit.sort()


# 7. Print out the list again.
#print(fruit)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
#for list in fruit:
  #print(list)


# 2. Print the numbers 1 to 100 (including the number 100).
#for number in range(1,101):
  #print(number)


# 3. Print all odd numbers from 1 to 100.
#for number in range(1, 101, 2):
  #print(number)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
yearsnotheld = [1916, 1940, 1944, 2020]
for years in range(1896, 2023, 4):
  if years not in yearsnotheld:
    print(years)
  

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
numbers = [2, 17, 80, 7, 23, 91, 11, 38, 79, 40]
even_count = 0
odd_count = 0

for x in numbers:
    if x % 2 == 0:
        even_count = even_count + 1
    else:
        # This is short hand for the line above
        odd_count = odd_count + 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")

 


# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
names = ["Louisa", "Shamil", "Natasha", "Pablo", "Elias"]
for name in names:
  print("Hello " + name + ".")


# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
for letter in word:
  print(letter)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
numbers2 = [2, 17, 80, 7, 23]
sqrnumbers2 = []
for number in numbers2:
  sqrnumbers2.append(number ** 2)
print(sqrnumbers2)


# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
names2 = ["Louisa", "Shamil", "Natasha", "Pablo", "Elias"]
titlename = []
for name in names:
  titlename.append("Dr. " + name)

print(titlename)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
for numbers3 in range(1, 101):
  if (numbers3 % 3 == 0) and (numbers3 % 5 == 0):
    print("FizzBuzz")
  elif numbers3 % 3 == 0:
    print("Fizz")
  elif numbers3 % 5 == 0:
    print("Buzz")
  else:
    print(numbers3)
  