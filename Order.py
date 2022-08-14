class Order:
    TAX_RATE = 0.07
    status = ["Creating", "Payment", "Cooking", "Quality Check", "Ready", "Out for Delivery"]
    price = 0
    tax = price * TAX_RATE
    total_cost = price + tax
    cart = []

    def __init__(self):
        print("New order created")

    def add_to_cart(self, items):
        self.cart.append(items)

    def remove_from_cart(self, item):
        self.cart.remove(item)

