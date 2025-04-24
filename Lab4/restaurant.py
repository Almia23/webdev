class Restaurant:
    def __init__(r):
        r.menu, r.tables, r.orders = {}, [], []
    def add_item_to_menu(r, name, price): r.menu[name] = price
    def book_tables(r, num): r.tables.append(num)
    def customer_order(r, item): r.orders.append(item)
    def show(r): print("Menu:", r.menu); print("Tables:", r.tables); print("Orders:", r.orders)

res = Restaurant()
res.add_item_to_menu("Pizza", 150)
res.add_item_to_menu("Burger", 80)
res.book_tables(5)
res.customer_order("Pizza")
res.show()