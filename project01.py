import tkinter as tk

root = tk.Tk()
root.title('Reminder')
lbl = tk.Label(text='Add reminder')
lbl.pack(pady=10)
set_btn = tk.Button(text='Add remender', command=set)
set_btn.pack()
root.mainloop()