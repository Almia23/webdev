class Inventory:
    def __init__(i): i.data = {}
    def add_item(i, id, name, count, price): i.data[id] = {"name": name, "count": count, "price": price}
    def update_item(i, id, count=None, price=None):
        if count is not None: i.data[id]["count"] = count
        if price is not None: i.data[id]["price"] = price
    def check_item_details(i, id): print(i.data.get(id))

inv = Inventory()
inv.add_item(101, "Pen", 50, 10)
inv.update_item(101, count=60)
inv.check_item_details(101)