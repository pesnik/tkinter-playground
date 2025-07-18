"""
Hello World Tkinter Application
===============================

Your first Tkinter application - a simple window with a label and button.

Challenge: Run this code and understand each component.
Then modify it to add your own widgets!
"""

import tkinter as tk
from tkinter import messagebox


def on_button_click():
    """Handle button click event"""
    messagebox.showinfo("Hello!", "Welcome to Tkinter Playground!")


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello Tkinter!")
    root.geometry("300x200")
    
    # Create a label
    label = tk.Label(
        root, 
        text="Welcome to Tkinter Playground!",
        font=("Arial", 14),
        fg="blue"
    )
    label.pack(pady=20)
    
    # Create a button
    button = tk.Button(
        root,
        text="Click Me!",
        command=on_button_click,
        bg="lightblue",
        font=("Arial", 12)
    )
    button.pack(pady=10)
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
