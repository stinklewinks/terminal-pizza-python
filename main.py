from Pizza import Pizza
from Order import Order

# This is a demo pizza app
# I want to add a menu a user can navigate through
# I want to add a list of toppings a user can choose from
# I want to add a delivery system
size_choices = ["small", "medium", "large", "x-large"]
style_choices = ["pan", "hand-tossed", "thin crust"]

print("""Welcome to PizzaPy Orderator!!

Here you can build your own pizza, 
Browse our pies,
or check out our deals!

""")
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
print("This is your pizza so far: ")
print(pepperoni.toppings)
new_order.add_to_cart(pepperoni)
status = new_order.status[1]
print(status)
print("It's time for payment.")
