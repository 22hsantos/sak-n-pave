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
    def __init__(self,key,stock,price):
        self.key = key
        self.stock = stock
        self.price = price

def update_data(key,item):
    """Updates inventory data in pickle file."""
    with open('inventory.pkl', 'rb') as f:
        data = pickle.load(f)
    data[key] = item
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(data, f)
    load_data()

def load_data():
    """Loads stock data from inventory pickle file."""
    if not os.path.exists('inventory.pkl'):
        os.system('python seed.py')
    with open('inventory.pkl', 'rb') as f:
        return pickle.load(f)

inventory = load_data()

class MainWindow:
    """
    Main application class for navigation and stock display.
    """
    def __init__(self,parent):

        #layout configuration 
        self.parent = parent
        parent.geometry("400x400")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        #region for main menu screen

        """Main menu screen for navigation"""

        #main menu frame
        self.main_menu_frame = Frame(parent,bg="white")
        self.main_menu_frame.grid(column=0, row=0, sticky=NSEW)
        self.main_menu_frame.grid_rowconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(0, weight=1)

        #header frame
        self.header_frame = Frame(self.main_menu_frame,bg="lightblue")
        self.header_frame.grid(column=0, row=0, sticky=NSEW)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)

        #header label
        self.header_label = Label(self.header_frame, text="SaknPave Inventory System", font=("Arial", 16), bg="lightblue")
        self.header_label.grid(column=0, row=0, sticky=NSEW)

        #navigation frame
        self.navi_frame = Frame(self.main_menu_frame,bg="white")
        self.navi_frame.grid(column=0, row=1, sticky=NSEW)
        self.navi_frame.grid_columnconfigure(0, weight=1)

        self.btn_frame = Frame(self.navi_frame,bg="white")
        self.btn_frame.grid(column=0,row=0,padx=40,pady=50,sticky= NSEW)
        self.btn_frame.grid_rowconfigure(0,weight=1)
        self.btn_frame.grid_columnconfigure(0,weight=1)

        #find stock button
        find_stock_btn = Button(
            self.btn_frame,
            text= "find stock",
            command= self.find_stock,
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
            command= self.show_all_stock,
            padx=20,
            pady=5
            )
        show_all_btn.grid(column=0,row=1, pady=3)

        #manage stock button
        self.manage_stock_btn = Button(
            self.btn_frame,
            text= "manage stock",
            command= self.manage_stock,
            font=("Arial", 10),
            padx=20,
            pady=5
            )
        self.manage_stock_btn.grid(column=0,row=2, pady=3)

        #endregion
    
        #region for find stock screen
        #find stock frame
        self.find_stock_frame = Frame(parent)
        self.find_stock_frame.grid(column=0, row=0, sticky=NSEW)
        self.find_stock_frame.grid_columnconfigure(0,weight=1)
        self.find_stock_frame.grid_rowconfigure(0,weight=1)
        self.find_stock_frame.grid_rowconfigure(1,weight=1)
        self.find_stock_frame.grid_rowconfigure(2,weight=1)

        #find stock header frame
        self.find_stock_header = Frame(self.find_stock_frame,bg="lightblue")
        self.find_stock_header.grid(column=0, row=0, sticky=NSEW,columnspan=2)
        self.find_stock_header.grid_rowconfigure(0, weight=1)
        self.find_stock_header.grid_columnconfigure(0, weight=1)

        #find stock header label
        self.find_stock_header_label = Label(
            self.find_stock_header,
            text="Find stock",
            font=("Arial", 16),
            bg="lightblue",
            pady=20
        )
        self.find_stock_header_label.grid(column=0, row=0, sticky=NSEW)

        #search bar
        self.search_entry = Entry(self.find_stock_frame)
        self.search_entry.grid(column=0,row=1,padx=10,pady=10,sticky=EW)

        #search button
        search_btn = Button(
            self.find_stock_frame,
            text="Search",
            command=self.search_inventory
        )
        search_btn.grid(column=1,row=1,padx=10,pady=5,sticky=E)
        self.find_stock_frame.grid_remove()
        #endregion for find stock screen

        #region for show inventory screen

        #show inventory frame
        self.show_all_frame = Frame(parent)
        self.show_all_frame.grid(column=0, row=0, sticky=NSEW)
        self.show_all_frame.grid_columnconfigure(0,weight=1)

        #show inventory header frame
        self.inventory_header = Frame(self.show_all_frame,bg="lightblue")
        self.inventory_header.grid(column=0, row=0, sticky=NSEW)
        self.inventory_header.grid_rowconfigure(0, weight=1)
        self.inventory_header.grid_columnconfigure(0, weight=1)

        #header label
        self.header_label = Label(
            self.inventory_header,
            text="Showing all stock",
            font=("Arial", 16),
            bg="lightblue",
            pady=20
            )
        self.header_label.grid(column=0, row=0, sticky=NSEW)

        #show inventory content frame
        self.inventory_content = Frame(self.show_all_frame)
        self.inventory_content.grid(column=0, row=1, sticky=NSEW)
        self.inventory_content.grid_columnconfigure(0,weight=1)

        for index, (key, item) in enumerate(inventory.items()):
            self.results(index, key, item, self.inventory_content)

        self.show_all_frame.grid_remove()
        #endregion for show inventory screen

        #region for item details screen

        #item details frame
        self.item_details_frame = Frame(parent,bg="white")
        self.item_details_frame.grid(column=0, row=0, sticky=NSEW)
        self.item_details_frame.grid_columnconfigure(0,weight=1)
        self.item_details_frame.grid_columnconfigure(1,weight=1)
        self.item_details_frame.grid_rowconfigure(1,weight=1)

        #item details header frame
        self.item_details_header = Frame(self.item_details_frame,bg="lightblue")
        self.item_details_header.grid(column=0, row=0, sticky=NSEW,columnspan=2)
        self.item_details_header.grid_rowconfigure(0, weight=1)
        self.item_details_header.grid_rowconfigure(2, weight=1)
        self.item_details_header.grid_columnconfigure(0, weight=1)

        #item details header label
        self.item_details_header_label = Label(
            self.item_details_header,
            text="Item details",
            font=("Arial", 16),
            bg="lightblue",
            pady=50
            )
        self.item_details_header_label.grid(column=0, row=0, sticky=NSEW,columnspan=2)

        #item details content frame
        self.item_details_content = Frame(self.item_details_frame,bg="white")
        self.item_details_content.grid(column=0, row=1, sticky=NSEW)
        self.item_details_content.grid_columnconfigure(0,weight=1)
        self.item_details_content.grid_rowconfigure(0,weight=1)

        self.sku_label = Label(
            self.item_details_frame,
            text="Stock Code: 1111",
            bg="white"
            )
        self.sku_label.grid(column=0,row=0,sticky=SW)

        self.name_label = Label(
            self.item_details_frame,
            text="Apple ",
            font=("Arial", 20),
            bg="white"
            )
        self.name_label.grid(column=0,row=1)

        self.stock_label = Label(
            self.item_details_frame,
            text= "In Stock: 3"
            )
        self.stock_label.grid(column=0,row=2,sticky=SW)

        self.price_label = Label(
            self.item_details_frame,
            text="$1.99",
            font=("Arial", 25),
            bg="white"
            )
        self.price_label.grid(column=1,row=1)

        self.item_details_frame.grid_remove()
        #endregion for item details screen

        #region for modify stock screen

        #modify stock frame
        self.modify_stock_frame = Frame(parent)
        self.modify_stock_frame.grid(column=0, row=0, sticky=NSEW)
        self.modify_stock_frame.grid_columnconfigure(0,weight=1)
        self.modify_stock_frame.grid_rowconfigure(0,weight=1)

        #modify stock header frame
        self.modify_stock_header = Frame(self.modify_stock_frame,bg="lightblue")
        self.modify_stock_header.grid(column=0, row=0, sticky=NSEW,columnspan=2)
        self.modify_stock_header.grid_rowconfigure(0, weight=1)
        self.modify_stock_header.grid_rowconfigure(2, weight=1)
        self.modify_stock_header.grid_columnconfigure(0, weight=1)

        #modify stock header label
        self.modify_stock_header_label = Label(
            self.modify_stock_header,
            text="Modify Stock",
            font=("Arial", 16),
            bg="lightblue",
            pady=50
            )
        self.modify_stock_header_label.grid(column=0, row=0, sticky=NSEW,columnspan=2)

        #modify item labels
        self.modify_name_label = Label(self.modify_stock_frame, text="Name:")
        self.modify_name_label.grid(column=0,row=1,sticky=NSEW)

        self.modify_stock_label = Label(self.modify_stock_frame, text="Stock:")
        self.modify_stock_label.grid(column=0,row=2,sticky=NSEW)

        self.modify_price_label = Label(self.modify_stock_frame, text="Price:")
        self.modify_price_label.grid(column=0,row=3,sticky=NSEW)

        self.modify_stock_frame.grid_remove()
        #endregion for modify stock screen

        #region for manage stock screen


        #manage stock frame
        self.manage_stock_frame = Frame(parent,bg="white")
        self.manage_stock_frame.grid(column=0, row=0, sticky=NSEW)
        self.manage_stock_frame.grid_columnconfigure(0, weight=1)

        #manage stock header frame
        self.manage_stock_header_frame = Frame(self.manage_stock_frame,bg="lightblue",pady=20)
        self.manage_stock_header_frame.grid(column=0, row=0, sticky=NSEW,columnspan=2)
        self.manage_stock_header_frame.grid_rowconfigure(0, weight=1)
        self.manage_stock_header_frame.grid_columnconfigure(0, weight=1)

        #manage stock header label
        self.manage_stock_header_label = Label(self.manage_stock_header_frame, text="Manage Stock", font=("Arial", 16), bg="lightblue")
        self.manage_stock_header_label.grid(column=0, row=0, sticky=NSEW)

        #manage stock content frame
        self.manage_stock_content_frame = Frame(self.manage_stock_frame,bg="white")
        self.manage_stock_content_frame.grid(column=0, row=1, sticky=NSEW)
        self.manage_stock_content_frame.grid_rowconfigure(0, weight=1)
        self.manage_stock_content_frame.grid_columnconfigure(0, weight=1)

        for index, (key, item) in enumerate(inventory.items()):
            self.results(index, key, item, self.manage_stock_content_frame)
            self.item_details_btn.config(text="Modify", command=lambda key=key, item=item: self.modify_item(key,item))
        
        add_item_btn = Button(
            self.manage_stock_content_frame,
            text="Add new item",
            command=self.add_item,
            padx=20,
            pady=5
        )
        add_item_btn.grid(column=1, row=100, padx=10, pady=5, sticky=SE)

        self.manage_stock_frame.grid_remove()
        #endregion for manage stock screen

        #region for add stock screen

        #frame for add stock screen
        self.add_stock_frame = Frame(parent)
        self.add_stock_frame.grid(column=0, row=0, sticky=NSEW)
        self.add_stock_frame.grid_columnconfigure(0, weight=1)
        self.add_stock_frame.grid_rowconfigure(0, weight=1)

        #header frame for add stock screen
        self.add_stock_header_frame = Frame(self.add_stock_frame,bg="lightblue",pady=20)
        self.add_stock_header_frame.grid(column=0, row=0, sticky=NSEW,columnspan=2)
        self.add_stock_header_frame.grid_rowconfigure(0, weight=1)
        self.add_stock_header_frame.grid_columnconfigure(0, weight=1)

        #header label for add stock screen
        self.add_stock_header_label = Label(
            self.add_stock_header_frame,
            text="Add new stock",
            font=("Arial", 16),
            bg="lightblue"
            )
        self.add_stock_header_label.grid(column=0, row=0, sticky=NSEW)

        #new item labels
        self.add_name_label = Label(self.add_stock_frame, text="Name:")
        self.add_name_label.grid(column=0,row=1,sticky=NSEW)

        self.add_stock_label = Label(self.add_stock_frame, text="Stock:")
        self.add_stock_label.grid(column=0,row=2,sticky=NSEW)

        self.add_price_label = Label(self.add_stock_frame, text="Price:")
        self.add_price_label.grid(column=0,row=3,sticky=NSEW)

        #modify item entries
        self.add_name_entry = Entry(self.add_stock_frame)
        self.add_name_entry.grid(column=1,row=1,sticky=NSEW,padx=10,pady=5)

        self.add_stock_entry = Entry(self.add_stock_frame)
        self.add_stock_entry.grid(column=1,row=2,sticky=NSEW,padx=10,pady=5)

        self.add_price_entry = Entry(self.add_stock_frame)
        self.add_price_entry.grid(column=1,row=3,sticky=NSEW,padx=10,pady=5)

        #modify item button
        save_btn = Button(
            self.add_stock_frame,
            text="Save",
            command=lambda: self.save_item_changes(key,item),
            padx=20,
            pady=5
        )
        save_btn.grid(column=1,row=4, pady=10, sticky=W)

        self.add_stock_frame.grid_remove()
        #endregion for add stock screen

    def find_stock(self):
        self.find_stock_frame.grid()
        self.make_return_button(self.find_stock_frame)
    def search_inventory(self):
        """
        takes user input and searches inventory.pkl for a match,
        displays matching items
        """
        #user input
        search_input = self.search_entry.get()

        #item
        search_result = inventory.get(search_input)

        if search_result:
            self.item_details(search_input, search_result)
        else:
            for key, item in inventory.items():
                if item.key == search_input.lower():
                    self.item_details(item.key, item)
            messagebox.showinfo("Not found", "Item not found in inventory.")
    def show_all_stock(self):
        self.show_all_frame.grid()
        self.make_return_button(self.show_all_frame)
    def modify_item(self,key,item):
        self.manage_stock_frame.grid_remove()
        self.modify_stock_frame.grid()

        #modify item entries
        self.modify_name_entry = Entry(self.modify_stock_frame)
        self.modify_name_entry.grid(column=1,row=1,sticky=NSEW,padx=10,pady=5)
        self.modify_name_entry.insert(0, item.key)

        self.modify_stock_entry = Entry(self.modify_stock_frame)
        self.modify_stock_entry.grid(column=1,row=2,sticky=NSEW,padx=10,pady=5)
        self.modify_stock_entry.insert(0, item.stock)

        self.modify_price_entry = Entry(self.modify_stock_frame)
        self.modify_price_entry.grid(column=1,row=3,sticky=NSEW,padx=10,pady=5)
        self.modify_price_entry.insert(0, item.price)

        #modify item button
        save_btn = Button(
            self.modify_stock_frame,
            text="Save",
            command=lambda: self.save_item_changes(key,item),
            padx=20,
            pady=5
        )
        save_btn.grid(column=1,row=4, pady=10, sticky=W)
        self.make_return_button(self.modify_stock_frame)
    def make_return_button(self,source):
        return_btn = Button(
            source,
            text="Return",
            command= source.grid_remove,
            padx=10,
            pady=5
        )
        return_btn.grid(column=0,row=100,padx=10,pady=5,sticky=SW)
    def item_details(self,key,item):
        self.item_details_frame.grid()
        self.sku_label.config(text=f"Stock Code: {key}")
        self.name_label.config(text=f"{item.key}")
        self.stock_label.config(text=f"In Stock: {item.stock}")
        self.price_label.config(text=f"${item.price:.2f}")

        if item.stock < 3:
            messagebox.showwarning("Low stock", f"{item.key} is low in stock!")
            self.stock_label.config(fg="red")
        else:
            self.stock_label.config(fg="black")
        
        self.make_return_button(self.item_details_frame)
    def results(self,index,key,item,source):
        #item SKU
        result_sku = Label(source, text=f"Stock Code: {key}")
        result_sku.grid(column=0,row=index)

        #item name
        result_name = Label(source,text=f"{item.key}")
        result_name.grid(column=1,row=index,sticky=NSEW)

        #item stock
        result_stock = Label(source, text=f"stock: {item.stock}")
        result_stock.grid(column=2,row=index)

        self.item_details_btn = Button(
            source,
            text="Details",
            command=lambda key = key, item=item: self.item_details(key,item)
        )
        self.item_details_btn.grid(column=3,row=index, padx=10)
    def manage_stock(self):
        self.manage_stock_frame.grid()
        self.make_return_button(self.manage_stock_frame)
    def add_item(self):
        self.add_stock_frame.grid()
        self.make_return_button(self.add_stock_frame)
    def save_item_changes(self,key,item):

        new_name = self.modify_name_entry.get()
        new_stock = self.modify_stock_entry.get()
        new_price = self.modify_price_entry.get()

        if not new_name:
            messagebox.showerror("Error", "Name cannot be empty.")
            return
        if not new_stock.isdigit():
            messagebox.showerror("Error", "Stock must be a number.")
            return
        if not new_price.isdigit():
            messagebox.showerror("Error", "Price must be a number.")
            return

        item.key = new_name
        item.stock = int(new_stock)
        item.price = int(new_price)

        update_data(key,item)

        messagebox.showinfo("Success", "Item updated successfully.")

        self.modify_stock_frame.grid_remove()
        self.item_details(key, item)

if __name__ == "__main__":
    root = Tk()
    main = MainWindow(root)
    root.mainloop()