from Pizza import Pizza

# This is a demo pizza app
# I want to add a menu a user can navigate through
# I want to add a list of toppings a user can choose from
# I want to add a delivery system

pepperoni = Pizza()

pepperoni.add_topping("Pepperoni")
pepperoni.pizza_size("Large")
pepperoni.cook_time = "Well Done"
pepperoni.add_cheese("Extra Cheese")
pepperoni.crust_type("Butter Garlic")

print("This is what your pizza looks like: " + str(pepperoni.toppings))
