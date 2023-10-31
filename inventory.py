inventory = {"books" : 50, "pen": 10, "Eraser" : 5, "sharpner" : 15}
print(inventory)
added_item = {"pencils": 20}
inventory.update(added_item)
print(f"added item list is : {inventory}")
update_quantity = {"books": 100, "pen" : 20}
inventory.update(update_quantity)
print(f"updated list is {update_quantity}")
print(f"final list is : {inventory}")