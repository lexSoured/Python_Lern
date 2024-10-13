import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import datetime 
import time
import pygame

t_stamp = 0
music = False

def set_reminder():
    global t_stamp 
    remind = simpledialog.askstring('Reminder time', 'Enter reminder\n(in 24 hour)', initialvalue="HH:MM")
    if remind and len(remind) == 5 and ':' in remind:
            try:
                hour, minute = map(int, remind.split(':'))
                now = datetime.datetime.now()
                time_rem = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                if time_rem <= now:
                    time_rem += datetime.timedelta(days=1)  
                t_stamp = time_rem.timestamp()
                messagebox.showinfo('Success', f'Reminder set for {time_rem.strftime("%H:%M")}')
            except ValueError as e:
                messagebox.showerror('Error', f'Invalid time format: {e}')
    elif remind:
            messagebox.showerror('Error', 'Invalid time format. Please enter HH:MM.')


def check_reminder():
    global t_stamp
    if t_stamp:
        now = time.time()
        if now >= t_stamp:
            play_sound()
            t_stamp = None
    root.after(10000, check_reminder)


def play_sound():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load(r'./music/Ariis - Funk Do Bounce.mp3')
    pygame.mixer.music.play()

def stop_reminder():
    global music
    if music:
         pygame.mixer.music.stop()
         music = False
    lbl.config(text='Add new Reminder')

     
 
root = tk.Tk()
root.title('Reminder')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.update_idletasks() 

lbl = tk.Label(text='Add Reminder', font=('Comic Sens', 16))
lbl.pack(pady=10)
set_btn = tk.Button(text='Set remender', font=('Comic Sens', 12), command=set_reminder)
set_btn.pack(pady=10, ipadx=5, ipady=5)

stop_btn = tk.Button(text='Stop sound', font=('Comic Sens', 12), command=stop_reminder)
stop_btn.pack(pady=10, ipadx=5, ipady=5)


check_reminder()

root.mainloop()