import pickle

class InventoryItem:
    """
    support class for creating Inventory items.
    """
    def __init__(self,key,stock,price):
        self.key = key
        self.stock = stock
        self.price = price

initial_inventory = {
"001": InventoryItem("Apple", 5, 5),
"002": InventoryItem("Orange", 6, 3),
"003": InventoryItem("Banana", 3, 10)
}

with open("inventory.pkl", "wb") as f:
    pickle.dump(initial_inventory, f)
print("Inventory seeded successfully.")