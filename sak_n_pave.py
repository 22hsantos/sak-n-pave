"""
SaknPave: Graphical inventory system

This script uses a GUI to present stock in a readable format.
Users can search for specific items from a simple txt file database.
Users can navigate through the list of stock through various buttons.
Users can also add, remove, or modify stock information.
"""

from tkinter import *
from tkinter import messagebox
import pickle
import os

class InventoryItem:
    """
    support class for creating Inventory items.
    """
    def __init__(self,name,stock,price):
        self.name = name
        self.stock = stock
        self.price = price

all_stock = {
"001": InventoryItem("Apple", 5, 5),
"002": InventoryItem("Orange", 6, 3)
}

inventory_order = []

def write_data():
    """Writes the current stock data to inventory pickle file."""
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(all_stock, f)

def load_data():
    """Loads stock data from inventory pickle file."""

    if not os.path.exists('inventory.pkl'):
        write_data()
    with open('inventory.pkl', 'rb') as f:
        return pickle.load(f)


class MainWindow:
    """
    Main application class for navigation and stock display.
    """
    def __init__(self,parent):
        #layout configuration 
        self.parent = parent
        parent.geometry("400x400")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        #header frame
        self.header_frame = Frame(self.parent,bg= "lightyellow")
        self.header_frame.grid(column=0,row=0, sticky= NSEW)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_remove()

        #header label
        self.header_label = Label(
            self.header_frame,
            text= "Welcome to Sak n Pave Inventory system.",
            font=("Arial", 12),
            background= "lightyellow"
        )
        self.header_label.grid(column=0,row=0)

        #navigation frame
        self.navi_frame = Frame(self.parent,bg= "white")
        self.navi_frame.grid(column=0, row=1, sticky= NSEW)
        self.navi_frame.grid_rowconfigure(1, weight=1)
        self.navi_frame.grid_columnconfigure(0,weight=1)
        self.navi_frame.grid_remove()

        #buttons frame
        self.btn_frame = Frame(self.navi_frame,bg="white")
        self.btn_frame.grid(column=0,row=0,padx=40,pady=50,sticky= NSEW)
        self.btn_frame.grid_rowconfigure(0,weight=1)
        self.btn_frame.grid_columnconfigure(0,weight=1)

        #find stock button
        find_stock_btn = Button(
            self.btn_frame,
            text= "find stock",
            font=("Arial", 10),
            padx=20,
            pady=5
        )
        find_stock_btn.grid(column=0,row=0,pady=3)

        #show all button
        show_all_btn = Button(
            self.btn_frame, 
            text= "Show all",
            font=("Arial", 10),
            command= self.display_all_stock,
            padx=20,
            pady=5
            )
        show_all_btn.grid(column=0,row=1, pady=3)

        #manage stock button
        stock_adjust_btn = Button(
            self.btn_frame,
            text= "manage stock",
            command=lambda: self.item_details(load_data().get("001"), load_data().get("001")),
            font=("Arial", 10),
            padx=20,
            pady=5
            )
        stock_adjust_btn.grid(column=0,row=2, pady=3)
        
        #show all frame
        self.show_all_frame = Frame(self.parent)
        self.show_all_frame.grid(column=0, row=1, sticky=NSEW)
        self.show_all_frame.grid_columnconfigure(0,weight=1)
        self.show_all_frame.grid_columnconfigure(1,weight=1)
        self.show_all_frame.grid_remove()

        #item details frame
        self.item_details_frame = Frame(parent)
        self.item_details_frame.grid(column=0,row=1,sticky=NSEW)
        self.item_details_frame.grid_columnconfigure(0,weight=1)
        self.item_details_frame.grid_columnconfigure(1,weight=1)
        self.item_details_frame.grid_remove()

        #modify item frame
        self.modify_frame = Frame(parent)
        self.modify_frame.grid(column=0,row=1,sticky=NSEW)
        self.modify_frame.grid_columnconfigure(0,weight=1)
        self.modify_frame.grid_columnconfigure(1,weight=1)
        self.modify_frame.grid_remove()

        self.main_menu()

    def main_menu(self):
        self.header_frame.grid()
        self.navi_frame.grid()

    def make_return_button(self,source):
        """Creates a return button for the source frame."""
        return_btn = Button(
            source,
            text="Return",
            command=lambda: self.return_to_header(source)
            )
        return_btn.grid(column=0, row=100, pady=5, sticky=SW)

    def return_to_header(self,source):#TODO:fix naming convention
        """Forgets the current screen and returns to the main menu."""
        source.grid_remove()
        self.header_frame.grid()
        self.navi_frame.grid()
        self.header_label.config(text="Welcome to Sak n Pave Inventory system.")

    def display_all_stock(self):
        """Display all stock items."""
        self.navi_frame.grid_remove()

        #change header label to "Showing All Stock"
        self.header_label.config(text="Showing All Stock")

        #shows show_all_frame
        self.show_all_frame.grid()

        self.result(self.show_all_frame)

        self.make_return_button(self.show_all_frame)
        #TODO: make the return button inside the header

    def result(self,source):
        """loads data in readable state and returns"""
        current_row = 0
        
        for name, item in load_data().items():
            
            #item SKU
            result_sku = Label(source, text=f"Stock Code: {name}")
            result_sku.grid(column=0,row=current_row)

            #item name
            result_name = Label(source,text=f"{item.name}")
            result_name.grid(column=1,row=current_row,sticky=NSEW)

            #item stock 
            result_stock = Label(source, text=f"stock: {item.stock}")
            result_stock.grid(column=2,row=current_row)

            item_details = Button(
                source,
                text="Details",
                command=lambda name = name, item=item: self.item_details(name,item)
            )
            item_details.grid(column=3,row=current_row, padx=10)

            current_row+= 1

    def item_details(self,key,item):
        print(key,item)
        self.header_label.config(text="Manage Stock")
        self.navi_frame.grid_remove()
        self.item_details_frame.grid()

        sku_label = Label(
            self.item_details_frame,
            text=f"Stock Code: {key}"
            )
        sku_label.grid(column=0,row=0,sticky=W)

        name_label = Label(
            self.item_details_frame,
            text=f"{item.name}",
            font=("Arial", 20)
            )
        name_label.grid(column=0,row=1)

        stock_label = Label(
            self.item_details_frame,
            text=f"In Stock: {item.stock}"
            )
        stock_label.grid(column=0,row=2,sticky=SW)

        price_label = Label(
            self.item_details_frame,
            text=f"${item.price:.2f}",
            font=("Arial", 25),
            bg="white"
            )
        price_label.grid(column=1,row=1)

        self.make_return_button(self.item_details_frame)
        modify_btn = Button(
            self.item_details_frame,
            text="Modify",
            command=lambda: self.manage_item(key,item)
        )
        modify_btn.grid(column=1,row=100,sticky=SE)

    def manage_item(self, key, item):
        self.item_details_frame.grid_remove()
        self.modify_frame.grid()
    
        #modify item entries
        self.modify_name_entry = Entry(self.modify_frame)
        self.modify_name_entry.grid(column=1,row=0,sticky=NSEW,padx=10,pady=5)

        self.modify_stock_entry = Entry(self.modify_frame)
        self.modify_stock_entry.grid(column=1,row=1,sticky=NSEW,padx=10,pady=5)

        self.modify_price_entry = Entry(self.modify_frame)
        self.modify_price_entry.grid(column=1,row=2,sticky=NSEW,padx=10,pady=5)
        
        #modify item labels
        self.modify_name_label = Label(self.modify_frame, text="Name:")
        self.modify_name_label.grid(column=0,row=0,sticky=NSEW)

        self.modify_stock_label = Label(self.modify_frame, text="Stock:")
        self.modify_stock_label.grid(column=0,row=1,sticky=NSEW)

        self.modify_price_label = Label(self.modify_frame, text="Price:")
        self.modify_price_label.grid(column=0,row=2,sticky=NSEW)

        save_btn = Button(
            self.modify_frame,
            text="Save",
            command=lambda: self.save_item_changes(key, item),
            padx=20,
            pady=5
        )
        save_btn.grid(column=1,row=3, pady=10, sticky=W)

    def save_item_changes(self, key, item):
        pass

if __name__ == "__main__":
    root = Tk()
    main = MainWindow(root)
    root.mainloop()
    write_data()
    load_data()
