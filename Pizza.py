class Pizza:
    toppings = []
    size = "small"
    cook_time = "Normal"
    pricing = {"Small": 7, "Medium": 8, "Large": 9, "X-Large": 11}

    def __init__(self):
        print("Time to build a pizza!")

    def pizza_size(self, size):
        self.size = size

    def add_topping(self, topping):
        self.toppings.append(topping)
        print("Added {topping} to your pizza.".format(topping=topping))

    def add_cheese(self, cheese_amt):
        self.toppings.append(cheese_amt)

    def crust_type(self, crust):
        self.toppings.append(crust)