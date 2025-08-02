import tkinter as tk

root = tk.Tk()
root.title("pack() Arguments Demo")
root.geometry("400x500")

# Demonstrate different combinations
tk.Label(root, text="1. Basic pack()", bg="red").pack()

tk.Label(root, text="2. With padx/pady", bg="green").pack(padx=10, pady=5)

tk.Label(root, text="3. Fill X", bg="blue").pack(fill="x", padx=20, pady=5)

tk.Label(root, text="4. Side=LEFT", bg="yellow").pack(side="left", padx=5)

tk.Label(root, text="5. Side=RIGHT", bg="orange").pack(side="right", padx=5)

# New frame for more complex examples
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, pady=10)

tk.Label(frame, text="6. Expand=True", bg="purple", fg="white").pack(
    fill="both", 
    expand=True, 
    padx=30, 
    pady=10
)

tk.Label(frame, text="7. Internal Padding", bg="pink").pack(
    ipadx=20, 
    ipady=10, 
    pady=5
)

# Anchor demonstration
anchor_frame = tk.Frame(root, bg="lightgray", height=80)
anchor_frame.pack(fill="x", padx=10, pady=10)
anchor_frame.pack_propagate(False)

tk.Label(anchor_frame, text="8. Anchor=CENTER", bg="cyan").pack(anchor="center")

root.mainloop()