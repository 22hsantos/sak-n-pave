"""
SaknPave: Graphical inventory system

This script uses a GUI to present stock in a readable format.
Users can search for specific items from a simple txt file database.
Users can navigate through the list of stock through various buttons.
Users can also add, remove, or modify stock information.
"""

from tkinter import *
from tkinter import messagebox

class MainWindow:
    """
    Main application class for navigation and stock display.
    """
    def __init__(self,parent):
        #layout configuration
        parent.geometry("400x400")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        #main menu title frame
        self.title_frame = Frame(parent,bg= "lightyellow")
        self.title_frame.grid(column=0,row=0, sticky= NSEW)
        self.title_frame.grid_rowconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(0, weight=1)

        #main menu title
        menu_title = Label(
            self.title_frame,
            text= "Welcome to Sak n Pave Inventory system.",
            font=("Arial", 12),
            background= "lightyellow"
        )
        menu_title.grid(column=0,row=0)

        #navigation frame
        self.navi_frame = Frame(parent,bg= "white")
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


if __name__ == "__main__":
    root = Tk()
    main = MainWindow(root)
    root.mainloop()
