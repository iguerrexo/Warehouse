"""

        program: Warehouse management system
        author: Nora Guerrero
        Description:
        1- Register new item
            id (auto generated)
            title (str)
            category (str)
            price (float)
            stock (int)

        2 - Display Catalog
        3 - Update stock
        4 - Remove item from catalog
        5 - Print Total stock value
        6 - Report - out of stock

"""
#imports
from menu import clear, print_menu, print_header, print_item
from item import Item
import pickle

#Global Vars
catalog = []
data_file = 'warehouse.data'

def serialize_catalog():
    global data_file
    writer = open('warehouse.data', 'wb') #create open a file to write binary
    pickle.dump(catalog, writer)
    writer.close() #close stream, realease the file
    print("**Data serialized!**")

def deserialize_catalog():
    try:
        global data_file
        reader = open(data_file, 'rb')
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)
        
        print("** Deserialized " + str(len(catalog)) + "items" )

    except:
        print("Error, cannot load data!")


def register_item():
    try: 
        print_header("Register New Item")
        title = input("Please provide the Title: ")
        cat = input("Please provide the Category: ")
        price = float(input("Please provide the Price: "))
        stock = int(input("Please provide the Stock: "))

        id = 1 
        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        how_many = len(catlog)
        print("You now have: "+ str(how_many)+ "item on catalog")

    #item.id = id
    #item.title = title
    #item.category = cat
    #item.price = price
    #item.stock = stock 

    #You are missing this:
    except ValueError:
        print('Error: incorrect value, try again')
    except:
        print("Error, Something went wrong")

def display_catalog():
    print_header("Your Current Catalog")
    for item in catalog:
        print_item(item)
        #print(
        #     str(item.id).rjust(3)
        #   + " | " + item.title.ljust(25) 
        #   + " | " + item.category.ljust(12) 
        #   + " | " + str(item.stock).rjust(12)
        #   + " | $" + str(item.price).rjust(15)
          
        #)

        #print('_' * 80)


def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)

def total_stock_value():
    total = 0.0
    for item in catalog:
        total += item.price * item.stock

    print("Total Value: " + str(total))
            

#instructions
deserialize_catalog()
input("Press enter to continue")

opc= ''
while(opc!='x'):
    clear()
    print_menu()

    opc = input('Please chose an option: ')


    #if comparisons
    if (opc == '1'):
        register_item()
        serialize_catalog()
    elif (opc == '2'):
        display_catalog()
    elif (opc == '6'):
        display_out_of_stock()


    input("Press enter to continue")

