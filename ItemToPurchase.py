# Andrew Cunningham
# CSC 500 Portfolio Project

# Attributes
#   item_name (string)
#   item_price (float)
#   item_quantity (int)
#   item_description (string)
# Default constructor
#   Item name is required, item's price = 0, item's quantity = 0, default description

# contains no AI code
# no code has been changed following the conclusion of the course


class ItemToPurchase:

    # constants added for module 6
    DEFAULT_PRICE = 0.0
    DEFAULT_QUANTITY = 0
    DEFAULT_DESCRIPTION = 'No Description'

    def __init__(
            self,
            *args):
        '''
        Attempts to cleanse item_price and item_quantity
        if only 1 number is given, price is assigned
        item_name: String
        item_price: float with 2 signifigant figures.
        item_quantity: int
        '''       

        if len(args) == 0:
            print("usage: item_name(required) item_price(float)(optional) item_quantity(int)(optional) item_description(optional)")
        if len(args) >= 1:
            # There is, at least, a name
            self.item_name = args[0].strip()

        # assign the rest of the defaults to update later
        self.item_price = self.DEFAULT_PRICE
        self.item_quantity = self.DEFAULT_QUANTITY
        self.item_description = self.DEFAULT_DESCRIPTION

        if len(args) >= 2:
            # either price, quantity, or description
            self.clean_input(self, args[1])
        if len(args) >= 3:
            # either price, quantity, or description
            self.clean_input(self, args[2], False)
        if len(args) == 4:
            # all of the parameters were supplied
            # with how clean_input works, only description remains
            self.item_description = args[3].strip() if args[3] and args[3].strip() else self.DEFAULT_DESCRIPTION
        

    @staticmethod
    def clean_input(self, input, check_price = True):
        '''
        Attempts to assign price, then quantity, then description.
        since the way clean_price works, every number will return a float
        check_price == False will skip price and attempt to update the quantity, True by default
        '''
        if(isinstance(input, str)):
            input = input.strip() 

        price = self.clean_price(input)
        if price and check_price:
            # price was supplied
            self.item_price = price
            return
        
        quantity = self.clean_int(input)
        if quantity:
            # quantity was supplied
            self.item_quantity = quantity
            return
        
        # description was given
        self.item_description = input
        

    @staticmethod
    def clean_price(raw_price):
        '''
        attempts to sanitize price by removing whitespace, $, and commas from the price
        returns a float with 2 decimals if successful
        returns False if fails
        '''

        # module 6
        if isinstance(raw_price, float):
            return round(raw_price, 2)

        try:

            cleaned = raw_price.strip()
            cleaned = cleaned.replace("$", "").replace(",","")

            return round(float(cleaned), 2)

        except:
            return False
    
    @staticmethod
    def clean_int(number):
        """
        Simple method to cast raw_quantity to an int and return False if an exception is raised.
        """
        if isinstance(number, int):
            return number

        try:
            return int(number)
        except:
            return False

    def get_total(self):
        '''
        returns quantity * price as a float
        '''
        return self.item_quantity * self.item_price

    def get_item_summary(self):
        '''returns: *name* *quantity* @$*price* = $ *total'''
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.get_total():.2f}"
    
    def get_item_description(self):
        return f"{self.item_name}: {self.item_description}"
    
    def has_default_price(self):
        return self.item_price == self.DEFAULT_PRICE
    
    def has_default_quantity(self):
        return self.item_quantity == self.DEFAULT_QUANTITY
    
    def has_default_description(self):
        return self.item_description == self.DEFAULT_DESCRIPTION
    
    def __str__(self):
        return f"{self.item_name}, {self.item_description}, ${self.item_price:.2f}, qty: {self.item_quantity}"
    
    def print_item_cost(self):
        print(self.get_item_summary())