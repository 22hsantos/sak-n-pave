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
    "apple": InventoryItem("Apple", 5, 5),
    "orange": InventoryItem("Orange", 6, 3)
}

def write_data():
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(all_stock, f)
def load_data():
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
        parent.grid_columnconfigure(0, weight=1)

        #header frame
        self.header_frame = Frame(parent,bg= "lightyellow")
        self.header_frame.grid(column=0,row=0, sticky= NSEW)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)

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
            font=("Arial", 10),
            padx=20,
            pady=5
            )
        stock_adjust_btn.grid(column=0,row=2, pady=3)

        #test frame
        self.test_frame = Frame(parent)
        #show all frame
        self.show_all_frame = Frame(parent)

    def make_return_button(self,source):
        """Creates a return button for the source frame."""
        return_btn = Button(
            source,
            text="Return to Main Menu",
            command=lambda: self.return_to_header(source)
            )
        return_btn.grid(column=3, row=0, pady=5)

    def return_to_header(self,source):
        """Forgets the current screen and returns to the main menu."""
        source.grid_remove()
        self.header_frame.grid()
        self.navi_frame.grid()

    def display_all_stock(self):
        """Display all stock items."""
        self.navi_frame.grid_remove()

        self.header_label.config(text="Showing All Stock")
        
        """self.show_all_frame.grid(column=0, row=0, sticky=NSEW)
        tst2 = Label(self.show_all_frame,text="this is show all frame.")
        tst2.grid(column=0,row=0)"""

        self.make_return_button(self.show_all_frame)

if __name__ == "__main__":
    root = Tk()
    main = MainWindow(root)
    root.mainloop()
    write_data()
    load_data()
