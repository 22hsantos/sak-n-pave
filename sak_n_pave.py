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
        parent.geometry("400x400")

        testlbl = Label(parent, text="This is the main window.")
        testlbl.pack()

if __name__ == "__main__":
    root = Tk()
    main = MainWindow(root)
    root.mainloop()
