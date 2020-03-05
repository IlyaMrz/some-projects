stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print('\nInventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k, v)
        item_total += int(v)
    print(f"\nTotal number of items in inventory is: {item_total}")


def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1


addToInventory(stuff, dragonLoot)
displayInventory(stuff)
