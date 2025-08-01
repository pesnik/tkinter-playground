import tkinter as tk

root = tk.Tk()
root.title('Button events')

def say_cheese(event):
  print(event)
  print("Say Cheese")

cheese_speaker = tk.Button(master=root, text='Click me', command=lambda: say_cheese("frankly speaking"))
cheese_speaker.bind('<Enter>', lambda event: print('event'))
cheese_speaker.pack(side=tk.LEFT)

root.mainloop()