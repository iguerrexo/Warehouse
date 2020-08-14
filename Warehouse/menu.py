import os

def print_menu():
    print("-" * 30)
    print("Warehouse mgn sys")
    print("-" * 30)

    print("[1]Register New Item")
    print("[2] Display Catalog")

    print("[6] Display out of stock items")
    print("[7] Total Stock Value")
    print("[8] List of categories")
    print("[x] Close")
    
def print_header(title):
    clear()
    print("_" * 80)
    print(title)
    print("_" * 80)
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def print_item(item):
    print(
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25) 
        + " | " + item.category.ljust(12) 
        + " | " + str(item.stock).rjust(11)
        + " | $" + str(item.price).rjust(15)
    )

    print('-' * 80)
