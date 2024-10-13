import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import datetime 
import time
import pygame

t_stamp = 0

def set():
    global t_stamp 
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
            print(time_rem)
        except Exception as e:
            messagebox.showerror('Error', {e})

def check():
    global t_stamp
    if t_stamp:
        now = time.time()
        if now >= t_stamp:
            # play_sound()
            t_stamp = None
    root.after(10000, check)


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r'./music/Ariis - Funk Do Bounce.mp3')
    pygame.mixer.music.play()
 
root = tk.Tk()
root.title('Reminder')
lbl = tk.Label(text='Add reminder')
lbl.pack(pady=10)
set_btn = tk.Button(text='Add remender', command=set)
set_btn.pack()
root.mainloop()