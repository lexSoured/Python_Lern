import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import datetime 

def set():
    remind = simpledialog.askstring('Reminder time', 'Enter reminder time format HH:MM(#in 24 hour clock)')
    if remind:
        try:
            hour = int(remind.split(':')[0])
            minute = int(remind.split(':')[1])
            now = datetime.datetime.now()
            print(now)
            time_rem = now.replace(hour=hour, minute=minute)
            print(time_rem)
            t_stamp = time_rem.timestamp()
            print(time_rem, t_stamp)
        except Exception as e:
            messagebox.showerror('Error', {e})

root = tk.Tk()
root.title('Reminder')
lbl = tk.Label(text='Add reminder')
lbl.pack(pady=10)
set_btn = tk.Button(text='Add remender', command=set)
set_btn.pack()
root.mainloop()