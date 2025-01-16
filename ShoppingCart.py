# Andrew Cunningham
# CSC500 - portfolio project

# contains no AI code
# no code has been changed following the conclusion of the course

'''

Methods
    __init__(self, customer_name: str, current_date='Jan 1, 2020', list_of_items = None)
    item_in_cart(self, item_name: str)
    add_item(item to purchase)
    remove_item(self, item_name: str)
    change_item_quantity(self, item_name: str, new_quantity: int)
    modify_item (item to change)
    get_num_items_in_cart()
    get_cost_of_cart()
    get_totals()
    print_total(self)
    print_descriptions()
    get_descriptions()
'''

import ItemToPurchase
from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, customer_name: str, current_date='Jan 1, 2020', list_of_items = None):
        '''customer_name = string
            current_date = string. Default = 'Jan 1 2020'
            list_of_items = list or ItemToPurchase

            Constructor does not type check, an invalid list of Items to Purchase might throw an error later.
        
        '''
        self.customer_name = customer_name
        self.current_date = current_date
        self.shopping_cart = list_of_items if list_of_items is not None else []

    def item_in_cart(self, item_name: str):
        '''checks to see if item_name is valid -> True if in cart, False otherwise
        Raises typeError if item_name is not a valid str
        '''
        if not isinstance(item_name, str):
            raise TypeError(f"ItemToPurchase.item_in_cart param must be a string")

        return any(item.item_name == item_name for item in self.shopping_cart)

    def add_item(self, item: ItemToPurchase):
        '''Adds item to shopping_cart -> None'''
        

        if self.item_in_cart(item.item_name):
            print(f"Oops, {item.item_name} is already in the cart! do you instead want to call modify?")
            return

        self.shopping_cart.append(item)

    def remove_item(self, item_name: str):
        '''Removes ItemToPurchase -> None
        outputs to console if item isn't found
        '''
        if not self.item_in_cart(item_name):
            print(f"{item_name} not found in cart. Nothing removed.")

        # shallow copy the shopping cart to enforce good practices
        for curr_item in self.shopping_cart[:]:
            if curr_item.item_name == item_name:
                self.shopping_cart.remove(curr_item)
                break

    def modify_item(self, item: ItemToPurchase):
        '''if the item current in the cart has a default price, quantity, or description, updates
        with args. -> nothing
        outputs and does nothing if item cannot be found
        '''
        if not self.item_in_cart(item.item_name):
            print(f"{item.item_name} not found in cart. Nothing modified.")

        for curr_item in self.shopping_cart[:]:
            if curr_item.item_name == item.item_name:
                if curr_item.has_default_quantity():
                    curr_item.item_quantity = item.item_quantity
                if curr_item.has_default_price():
                    curr_item.item_price = item.item_price
                if curr_item.has_default_description():
                    curr_item.item_description = item.item_description
                break
    
    def change_item_quantity(self, item_name: str, new_quantity: int):
        '''updates the item quantity for the given name -> nothing
        works even if item_quantity is not default'''

        if not isinstance(new_quantity, int):
            print("change_item_quantity new_quantity must be a int")
            return

        for curr_item in self.shopping_cart:
            if curr_item.item_name == item_name:
                curr_item.item_quantity = new_quantity
                return
            
        print(f"{item_name} not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        '''returns count of all quantities'''
        count = 0
        for item in self.shopping_cart:
            count += item.item_quantity
        
        return count

    def get_cost_of_cart(self):
        '''returns total cost of all items in cart as float'''
        total = 0.0
        for item in self.shopping_cart:
            total += item.item_price * item.item_quantity

        return total
    
    def get_totals(self):
        '''Returns a string of the stopping cart including the owner's name and
        The details of each item seperated by a newline
        *Name*'s Shopping Card
        Number of items: *number*
        each item summary
        '''
        result = ""
        result += f"{self.customer_name}'s Shopping Cart - {self.current_date}\n"
        result += f"Number of Items: {self.get_num_items_in_cart()}\n"
        for item in self.shopping_cart:
            result += f"{item.get_item_summary()}"
            result += "\n"
        result += f"Total: ${self.get_cost_of_cart():.2f}"

        return result

    def print_total(self):
        '''outputs total to console -> nothing'''
        if not self.shopping_cart:
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.get_totals())

    def get_descriptions(self):
        ''' returns a string of the shopping cart to include:
        *Name*'s Shopping Cart
        Item Description
        Each item description
        '''
        result = ""
        result += f"{self.customer_name}'s Shopping Cart - {self.current_date}\n"
        result += "Item Descriptions\n"
        for item in self.shopping_cart:
            result += f"{item.get_item_description()}"
            result += "\n"
        
        return result

    def print_descriptions(self):
        '''outputs shopping cart to console -> nothing'''
        print(self.get_descriptions())