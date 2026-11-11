items = ["pencil","eraser","notebook","sharpener","glue"]
stock_counts = [12,0,8,5,3]

inventory = {item: count for item, count in zip(items,stock_counts)}
print("Total Inventory:",inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("Stock items:",in_stock_items)

chosen_item = input("Choose your item.")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item,"is not in stock.")
    exit()

prices = [10,5,15,40,20]
markup = int(input("Enter the markup amount."))

markup_prices = list(map(lambda p:p + markup , prices))
print("Markup prices:",markup_prices)

item_index = items.index(chosen_item)
chosen_price = markup_prices[item_index]
print("Chosen item price after markup:",chosen_price)

inventory[chosen_item] = inventory[chosen_item] - 1
print(chosen_item,"purchased! Remaining stock:",inventory[chosen_item])

print("")
print("====SCHOOL STORE INVENTORY CHECKER====")
print("Item bought:",chosen_item)
print("Price of item:",chosen_price)
print("Updated inventory:",inventory)
print("======================================")