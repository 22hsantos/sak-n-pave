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

        #title frame
        self.title_frame = Frame(parent,bg= "lightyellow")
        self.title_frame.grid(column=0,row=0, sticky= NSEW)
        self.title_frame.grid_rowconfigure(0, weight=1)
        self.title_frame.grid_columnconfigure(0, weight=1)

        #navigation frame

        #main menu title
        menu_title = Label(
            self.title_frame,
            text= "Welcome to Sak n Pave Inventory system.",
            background= "lightyellow"
        )
        menu_title.grid(column=0,row=0)

if __name__ == "__main__":
    root = Tk()
    main = MainWindow(root)
    root.mainloop()
