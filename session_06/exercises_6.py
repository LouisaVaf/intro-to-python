# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".
#apple = {
#  "type": "Bramley",
 # "price": "0.39",
  #"colour": "Green"
#}
#print(apple)


# 2. Add the best before date to the dictionary - print the dictionary.
#apple["Best before date"] = "20/07/23"
#print(apple)


# 3. Change the price to 0.41 - print the dictionary.
#apple["price"] = "0.41"
#print(apple)


# 4. Set the apple to be on offer using a Boolean - print the dictionary.
#apple["offer"] = True
#print(apple)


# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.
#del(apple["offer"])
#print(apple)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.
#info = []
#name = None

#while name != "":
#  name = input("What is your name? ")
#  age = input("What is your age? ")
#  if name and age:
#    info.append({
#    "name": name,
#    "age": age
#  })
#print(info)



# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).
menu = [
  {"name": "lasagna", "price": "£15", "Veggie": False},
  {"name": "Pesto Pasta", "price": "£11", "Veggie": True},
  {"name": "Gheyme", "price": "£20", "Veggie": False},
  {"name": "Kebab", "price": "£25", "Veggie": False},
  {"name": "Pizza", "price": "£15", "Veggie": True}
]
print(menu)

for food in menu:
  if food["Veggie"]:
    print(food["name"])
    

# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.
