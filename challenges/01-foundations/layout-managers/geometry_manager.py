import tkinter as tk

root = tk.Tk()
root.geometry('300x400')

btn_frame = tk.Frame(root)
input_frame = tk.Frame(root)
gap_frame = tk.Frame(root)

input = tk.Text(input_frame, height=2, width=80)
input.pack()

buttons = [
    ((1, 0), "C"), ((1, 1), "±"), ((1, 2), "%"), ((1, 3), "÷"),
    ((2, 0), "7"), ((2, 1), "8"), ((2, 2), "9"), ((2, 3), "×"),
    ((3, 0), "4"), ((3, 1), "5"), ((3, 2), "6"), ((3, 3), "-"),
    ((4, 0), "1"), ((4, 1), "2"), ((4, 2), "3"), ((4, 3), "+"),
    ((5, 0), "0"), ((5, 2), "."), ((5, 3), "=")
]

for (row, col), num in buttons:
  btn = tk.Button(btn_frame, text=f'{num}', width=5, height=2)
  btn.grid(row=row, column=col)

for i in range(5):
  btn_frame.rowconfigure(i, weight=1)
for i in range(4):
  btn_frame.columnconfigure(i, weight=1)

input_frame.pack(padx=50)
gap_frame.pack(pady=10)
btn_frame.pack(side='bottom', fill='both', expand=True)

root.mainloop()