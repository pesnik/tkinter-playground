import tkinter as tk

# Window setup
root = tk.Tk()
root.title('Hello World App')
root.geometry('1200x800')

# utilities
def submit():
  print(f"Submitted {username.get()}")

# Widgets
## Label
label = tk.Label(master=root, text='Hello World')
## Entry
username = tk.Entry(master=root)
username.insert(0, 'Enter your text here')
## Button
clicker_button = tk.Button(master=root, text='Click me', command=lambda: print("Button Clicked"))
submitter_button = tk.Button(master=root, text='Submt', command=submit)
# Text widget
descriptor = tk.Text(master=root)

# Layout management
label.pack()
username.pack()
clicker_button.pack(pady=10)
submitter_button.pack(padx=10, side=tk.LEFT)
descriptor.pack(side=tk.LEFT)

# Main loop
root.mainloop()
