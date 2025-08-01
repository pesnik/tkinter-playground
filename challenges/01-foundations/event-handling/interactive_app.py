import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Interactive App')
root.geometry('200x100')

master_btn = tk.Button(master=root, text='klick')
master_btn.bind('<Button-1>', lambda event: messagebox.showinfo(title='<Button-1>', message='Left Click'))
master_btn.bind('<Button-3>', lambda event: messagebox.showinfo(title='<Button-3>', message='Right Click'))

master_btn.pack(pady=40)

root.mainloop()