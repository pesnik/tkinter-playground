import tkinter as tk

root = tk.Tk()
root.title("grid() Arguments Demo")
root.geometry("500x400")

# Basic positioning
tk.Label(root, text="1. Basic (row=0,col=0)", bg="red").grid(row=0, column=0)
tk.Label(root, text="2. (row=0,col=2)", bg="green").grid(row=0, column=2)
tk.Label(root, text="3. (row=2,col=0)", bg="blue").grid(row=2, column=0)

# Spanning
tk.Label(root, text="4. Columnspan=2", bg="yellow").grid(row=1, column=0, columnspan=2, sticky="ew")
tk.Label(root, text="5. Rowspan=2", bg="orange", height=4).grid(row=0, column=1, rowspan=2, sticky="ns")

# Padding
tk.Label(root, text="6. Padding", bg="purple", fg="white").grid(
    row=3, column=0, padx=10, pady=5, ipadx=5, ipady=5)

# Sticky positioning
frame = tk.Frame(root, width=150, height=80, bg="lightgray")
frame.grid(row=3, column=1, columnspan=2, padx=10)
frame.grid_propagate(False)

tk.Label(frame, text="NW", bg="cyan").grid(sticky="nw")
tk.Label(frame, text="SE", bg="magenta").grid(sticky="se")
tk.Label(frame, text="Center", bg="pink").grid(sticky="")

# Configure weights for better layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.mainloop()