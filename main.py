from Pizza import Pizza
from Toppings import Toppings
from Order import Order
from datetime import datetime
import time

# This is a demo pizza app
# I want to add a menu a user can navigate through
# I want to add a list of toppings a user can choose from
# I want to add a delivery system
size_choices = ["small", "medium", "large", "x-large"]
style_choices = ["pan", "hand-tossed", "thin crust"]
current_date = datetime.now()
print(current_date)
print("Welcome to PizzaPy Orderator!!")

time.sleep(1)
print("Here you can build your own pizza,")
time.sleep(1)
print("Browse our pies,")
time.sleep(1)
print("or check out our deals!")

new_order = Order()
status = new_order.status[0]
print(status)
pepperoni = Pizza()
print("Let's determine the size of the pizza")


def choose_size():
    counter = 0
    for size in size_choices:
        print(str(counter + 1) + ". " + size.title())
        counter += 1


choose_size()
size_choice = int(input("What size would you like your pizza to be? (Choose options 1-4): "))
pepperoni.add_topping(size_choices[size_choice - 1])
print(pepperoni.toppings)

print("Would you like to add extra cheese?")

user_choice = 'y'
while user_choice == 'y':
    cheese_choice = input("1.Yes or 2.No? (Select 1 or 2): ")
    if cheese_choice == 1:
        pepperoni.add_cheese("Extra Cheese")
    else:
        pepperoni.add_cheese("Regular Cheese")
    user_choice = input("Would you like to add more cheeses? y or n: ")

print("What style would you like your pizza to be?")


def choose_style():
    counter = 0
    for style in style_choices:
        print(str(counter + 1) + ". " + style.title())
        counter += 1


choose_style()
style_choice = int(input("Please choose 1-3: "))
pepperoni.toppings.append(style_choices[style_choice - 1])

print("Let's add some toppings!")


def choose_meats():
    counter = 0
    for meat in Toppings.toppings["meats"]:
        print(str(counter + 1) + ". " + meat)
        counter += 1


def meat_loop():
    meat_switch = 'y'
    while meat_switch == 'y':
        choose_meats()
        meat_choice = int(input("Please choose your toppings (Please select the # of your topping: "))
        pepperoni.toppings.append(Toppings.toppings["meats"][meat_choice - 1])
        meat_switch = input("Would you like to add more toppings? y/n: ")
        if meat_switch != 'y':
            print("That's not the right character. Please try again. Choose y or n")
            meat_switch = input("Would you like to add more toppings? y/n: ")
        elif meat_switch != 'n':
            print("That's not the right character. Please try again. Choose y or n")
            meat_switch = input("Would you like to add more toppings? y/n: ")
        else:
            print(pepperoni.toppings)


meat_loop()
print("This is your pizza so far: ")
print(pepperoni.toppings)


# Order starts cooking
