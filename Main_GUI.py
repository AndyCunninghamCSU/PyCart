# Andrew Cunningham
# Intro To Python portfolio project
# GUI practice

# Draws a GUI to interface with shopping cart modules developed during the course.

# disclaimer: Contains extensive AI-generated code.

from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
import tkinter as tk
from datetime import datetime

class ShoppingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCart Shopping Application")

        # Menu
        self.items_available = [
            {"name": "Hot Dog", "description": "Classic beef hot dog", "price": 3.50},
            {"name": "Coffee", "description": "Freshly brewed coffee", "price": 1.50},
            {"name": "Soda", "description": "Chilled soda", "price": 1.00},
            {"name": "Pretzel", "description": "Salted soft pretzel", "price": 2.00},
            {"name": "Ice Cream", "description": "Vanilla ice cream cone", "price": 2.50},
            {"name": "Bagel", "description": "Cream cheese bagel", "price": 2.75},
            {"name": "Sandwich", "description": "Ham and cheese sandwich", "price": 4.00},
            {"name": "Water", "description": "Bottled spring water", "price": 1.25}
        ]

        # Main frame for dynamic content
        self.main_frame = tk.Frame(self.root, padx=50, pady=50)
        self.main_frame.pack()

        # Customer name and date entries
        self.initialization_fields()

        # Shopping cart will be stored here
        self.shopping_cart = None

    def initialization_fields(self):
        # Customize the font size and entry width
        entry_font = ('Arial', 12)  # Define a larger font
        entry_width = 30  # Define a wider width for the entries

        # Customer name entry
        self.name_entry = tk.Entry(self.main_frame, fg='grey', font=entry_font, width=entry_width)
        self.name_default_text = 'Customer Name'
        self.name_entry.insert(0, self.name_default_text)
        self.name_entry.bind('<FocusIn>', lambda event: self.on_entry_click(event, self.name_default_text))
        self.name_entry.bind('<FocusOut>', lambda event: self.on_focusout(event, self.name_default_text))
        self.name_entry.pack(padx=20, pady=10)  # Increased padding for better layout

        # Date entry
        self.date_entry = tk.Entry(self.main_frame, fg='grey', font=entry_font, width=entry_width)
        self.date_default_text = 'Leave blank for today'
        self.date_entry.insert(0, self.date_default_text)
        self.date_entry.bind('<FocusIn>', lambda event: self.on_entry_click(event, self.date_default_text))
        self.date_entry.bind('<FocusOut>', lambda event: self.on_focusout(event, self.date_default_text))
        self.date_entry.pack(padx=20, pady=10)  # Increased padding for better layout

        # Submit button
        self.submit_button = tk.Button(self.main_frame, text='Create Shopping Cart', command=self.create_cart, padx=10, pady=5)
        self.submit_button.pack(padx=20, pady=10)  # Increased padding for better layout


    def on_entry_click(self, event, default_text):
        if event.widget.get() == default_text:
            event.widget.delete(0, tk.END)
            event.widget.config(fg='black')

    def on_focusout(self, event, default_text):
        if event.widget.get() == '':
            event.widget.insert(0, default_text)
            event.widget.config(fg='grey')

    def clear_frame(self):
        """ Destroy all widgets from a frame """
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def create_cart(self):
        customer_name = self.name_entry.get() if self.name_entry.get() != self.name_default_text else 'Anonymous'
        date = self.date_entry.get() if self.date_entry.get() != self.date_default_text else datetime.now().strftime('%B %d, %Y')
        self.shopping_cart = ShoppingCart(customer_name, date)
        # print(f"Created new shopping cart for {customer_name} on {date}")
        self.display_items()

    def display_items(self):
        self.clear_frame()
        self.quantity_entries = []  # List to hold references to quantity entry widgets

        # Display header for the cart
        header_label = tk.Label(self.main_frame, text=f"{self.shopping_cart.customer_name}'s Shopping Cart", font=('Arial', 14))
        header_label.grid(row=0, columnspan=3, sticky='w', padx=10, pady=10)

        # Retrieve and display the number of items and total cost
        num_items = self.shopping_cart.get_num_items_in_cart()
        total_cost = self.shopping_cart.get_cost_of_cart()
        cart_summary_label = tk.Label(self.main_frame, text=f"Total Items: {num_items}, Total Cost: ${total_cost:.2f}", font=('Arial', 14))
        cart_summary_label.grid(row=1, columnspan=3, sticky='w', padx=10, pady=10)

        # Display grid of items
        for idx, item in enumerate(self.items_available, start=2):
            tk.Label(self.main_frame, text=item["name"], width=15).grid(row=idx, column=0, sticky='w', padx=5, pady=2)
            tk.Label(self.main_frame, text=f"${item['price']:0.2f}", width=10).grid(row=idx, column=1, padx=5, pady=2)
            quantity_entry = tk.Entry(self.main_frame, width=5)
            quantity_entry.insert(0, "")
            quantity_entry.grid(row=idx, column=2, padx=5, pady=2)
            self.quantity_entries.append((item, quantity_entry))  # Store item and its corresponding entry widget

        # Buttons for updating cart and viewing details
        update_cart_button = tk.Button(self.main_frame, text="Update Cart", command=self.update_cart)
        update_cart_button.grid(row=len(self.items_available) + 2, column=0, columnspan=3, pady=10, sticky='ew')

        view_cart_button = tk.Button(self.main_frame, text="View Cart", command=self.view_cart)
        view_cart_button.grid(row=len(self.items_available) + 3, column=0, columnspan=1, pady=10, sticky='ew')

        view_descriptions_button = tk.Button(self.main_frame, text="View Descriptions", command=self.view_descriptions)
        view_descriptions_button.grid(row=len(self.items_available) + 3, column=2, columnspan=1, pady=10, sticky='ew')

    def update_cart(self):
        for item, entry in self.quantity_entries:
            try:
                # will throw a ValueError if blank
                quantity = int(entry.get())
                if quantity > 0:  # Only add items with a positive quantity
                    new_item = ItemToPurchase(item["name"], item["price"], quantity, item["description"])
                    if self.shopping_cart.item_in_cart(new_item.item_name):
                        self.shopping_cart.change_item_quantity(new_item.item_name, new_item.item_quantity)
                    else:
                        self.shopping_cart.add_item(new_item)
            except ValueError:
                # quantity was not an int
                continue

        # Assuming you have methods to handle adding/updating items in ShoppingCart
        self.display_items()

    def view_cart(self):
        # Clear the current UI components in the main frame
        self.clear_frame()

        # Get the totals from the shopping cart
        cart_totals = self.shopping_cart.get_totals()

        # Display the cart totals in the main frame
        cart_totals_label = tk.Label(self.main_frame, text=cart_totals, font=('Arial', 14), justify=tk.LEFT)
        cart_totals_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Provide a button to go back to the item display
        back_button = tk.Button(self.main_frame, text="Back to Items", command=self.display_items)
        back_button.pack(pady=10)

    def view_descriptions(self):
        # Clear the current UI components in the main frame
        self.clear_frame()

        # Get the totals from the shopping cart
        cart_totals = self.shopping_cart.get_descriptions()

        # Display the cart totals in the main frame
        cart_totals_label = tk.Label(self.main_frame, text=cart_totals, font=('Arial', 14), justify=tk.LEFT)
        cart_totals_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Provide a button to go back to the item display
        back_button = tk.Button(self.main_frame, text="Back to Items", command=self.display_items)
        back_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingApp(root)
    root.mainloop()
            