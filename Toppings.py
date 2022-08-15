class Toppings:
    toppings = {"meats": ["pepperoni", "italian sausage", "ham", "canadian bacon", "beef", "bacon", "grilled chicken"], "veggies": ["red onion", "bell pepper", "banana pepper", "mushrooms", "black olives"]}
    pizza_toppings = []
    extra_meat = False
    extra_veggies = False

    def __init__(self):
        print("Here are our toppings: ")

    def add_topping(self, topping):
        self.pizza_toppings.append(topping)
        print("You added {topping} to your pizza.".format(topping=topping))

    def set_extra_meat(self, choice):
        if choice == 'Yes':
            self.extra_meat = True
        else:
            print("You have declined extra meat.")

    def set_extra_veggies(self, choice):
        if choice == 'Yes':
            self.extra_veggies = True
        else:
            print("You have declined extra veggies.")
