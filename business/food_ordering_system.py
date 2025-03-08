# business/food_ordering_system.py

class FoodOrderingSystem:
    def __init__(self):
        # A simple menu
        self.menu = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Salad": 4.99,
            "Pasta": 7.99
        }
        self.order = {}

    def get_menu(self):
        return self.menu

    def add_item(self, item):
        if item in self.menu:
            self.order[item] = self.order.get(item, 0) + 1

    def remove_item(self, item):
        if item in self.order:
            self.order[item] -= 1
            if self.order[item] <= 0:
                del self.order[item]

    def get_order_summary(self):
        return self.order

    def get_total(self):
        return sum(self.menu[item] * qty for item, qty in self.order.items())
