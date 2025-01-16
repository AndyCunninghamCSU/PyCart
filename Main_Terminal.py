# Andrew Cunningham
# CSC 500 - Portfolio Project

# Implements a terminal interface for the shopping cart class

from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase

def print_menu():
    '''prints the menu -> nothing'''
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change Item Quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def add_item(shopping_cart):
    '''Gathers input from command line and attempts to add the item -> nothing'''
    print("ADD ITEM TO CART")
    item_name = input("Enter the item name: ")
    item_desc = input("Enter the item description: ")
    item_price = input("Enter the item price: ")
    item_quantity = input("Enter the item quantity: ")

    item = ItemToPurchase(item_name, item_price, item_quantity, item_desc)
    shopping_cart.add_item(item)

def remove_item(shopping_cart):
    '''gets item name and attempts to remove -> nothing'''
    print("REMOVE ITEM FROM CART")
    item_name = input("Enter name of item to remove: ")

    shopping_cart.remove_item(item_name)

def update_quantity(shopping_cart):
    '''gets item name and new quantity and attempts to update -> nothing'''
    print("CHANGE ITEM QUANTITY")
    item_name = input("Enter the item name: ")
    new_quantity = int(input("Enter the new quantity: ").strip())

    shopping_cart.change_item_quantity(item_name, new_quantity)

def handle_command(command, shopping_cart):
    ''' input the command straight off the terminal input and the shopping cart
        attempts to interpret the command and returns the needed function
        updates the shopping cart
    '''
    commands = {
        'a': add_item,
        'r': remove_item,
        'c': update_quantity,
        'i': shopping_cart.print_descriptions,
        'o': shopping_cart.print_total
    }

    command = command.strip()

    if command == 'q':
        # very simple implemenation of the quit command
        return 'q'
    
    func = commands.get(command)

    if not func:
        print("invalid command!")
        return

    if command in ['a', 'r', 'c']:
        func(shopping_cart)
    else:
        func()

def terminal_input():
    ''' Interface with the user via the terminal by containing the control loop
        calling handle_command when the user provides input
    '''
    print("Shopping Cart")
    
    customer_name = input("Enter Customer's Name: ")
    todays_date = input("Enter Today's Date: ")

    shopping_cart = ShoppingCart(customer_name, todays_date)

    print('Usage: option')
    print_menu()

    while True:
        command = input("Choose an option: ")
        if handle_command(command, shopping_cart) == 'q':
            break


if __name__ == '__main__':
    terminal_input()