''' Develop a python application to manage the activities in a grocery store. Create a class GroceryStore with attributes – ItemId, ItemName, Rate, StockInHand and ReorderLevel. Create a subclass called StationeryItems that has its specific attribute – Brand. Create another subclass called SoftDrinks which has an attribute – Manufacturer. Add methods in both the subclasses by name addNewItem() to add new items into the stock. Add method sellItem() that takes ItemName, and Quantity as input. Inside the method, check if, the item is available. If such an item is not available, raise an exception by name “ItemNotAvailable”. If the item is present and stock is insufficient, then raise an exception called “Insufficient_Stock” along with the name of the item. If sufficient stock
is available, then make the transaction and update the stock. If the stock of any item falls below the ReorderLevel, then raise an exception called “Item stock below ReorderLevel” and update the current stock by adding 50% of the current stock. While
adding new items to stock, check for the validity of all the fields like Rate should not be negative, StockInHand should be more than the ReorderLevel. If any of the above condition is not satisfied, then the item should not be added to the stock. Add methods
to print the complete stock details of all the items. Overload this method to print the details of a specific item.
Create a menu driven application to implement the above scenario.'''



class ItemNotAvailable(Exception):
    pass

class InsufficientStock(Exception):
    def __init__(self, item_name):
        self.item_name = item_name
        super().__init__(f"Insufficient stock for item: {item_name}")

class ItemStockBelowReorderLevel(Exception):
    pass

class GroceryStore:
    def __init__(self):
        self.stock = []

    def addNewItem(self, item_id, item_name, rate, stock_in_hand, reorder_level):
        if rate < 0 or stock_in_hand < reorder_level:
            print("Invalid item details. Item not added to stock.")
        else:
            item = {
                "ItemID": item_id,
                "ItemName": item_name,
                "Rate": rate,
                "StockInHand": stock_in_hand,
                "ReorderLevel": reorder_level
            }
            self.stock.append(item)

    def sellItem(self, item_name, quantity):
        for item in self.stock:
            if item["ItemName"] == item_name:
                if item["StockInHand"] < quantity:
                    raise InsufficientStock(item_name)
                else:
                    item["StockInHand"] -= quantity
                    if item["StockInHand"] < item["ReorderLevel"]:
                        item["StockInHand"] += int(item["ReorderLevel"] * 0.5)
                    print(f"Sold {quantity} {item_name}(s)")
                    return
        raise ItemNotAvailable

    def printStock(self):
        for item in self.stock:
            print(f"Item ID: {item['ItemID']}")
            print(f"Item Name: {item['ItemName']}")
            print(f"Rate: {item['Rate']}")
            print(f"Stock in Hand: {item['StockInHand']}")
            print(f"Reorder Level: {item['ReorderLevel']}")
            print("-----------")

class StationeryItems(GroceryStore):
    def __init__(self, brand):
        self.brand = brand
        GroceryStore.__init__(self)  # Call the parent class constructor directly

class SoftDrinks(GroceryStore):
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        GroceryStore.__init__(self)  # Call the parent class constructor directly

# Example usage:
stationery = StationeryItems("ABC")
stationery.addNewItem(1, "Pen", 10, 100, 20)
stationery.addNewItem(2, "Notebook", 50, 50, 10)

soft_drinks = SoftDrinks("XYZ")
soft_drinks.addNewItem(1, "Coke", 2, 200, 50)

try:
    stationery.sellItem("Pen", 50)
except ItemNotAvailable:
    print("Item not available.")
except InsufficientStock as e:
    print(e)

try:
    soft_drinks.sellItem("Coke", 250)
except ItemNotAvailable:
    print("Item not available.")
except InsufficientStock as e:
    print(e)

stationery.printStock()
soft_drinks.printStock()
