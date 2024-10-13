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
    if remind:
        time_str = remind.replace(' ', '').replace(':', '').replace('.', '').replace('-', '')
        if len(time_str) == 4 and time_str.isdigit():
            hour=int(time_str[:2])
            minute = int(time_str[2:])
            now = datetime.datetime.now()
            time_rem = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if time_rem <= now:
                time_rem += datetime.timedelta(days=1)  
            t_stamp = time_rem.timestamp()
            text = simpledialog.askstring('Reminder text',  '\t\tPlease enter reminder text\t\t\n\n\n')
            lbl.config(text=f'Reminder set for\n{time_rem.strftime("%H:%M")}\n for {text}')
        else:
            messagebox.showerror('Error', 'Invalid time format. Please enter HHMM or HH:MM.')
    else:
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
set_btn = tk.Button(text='Set remender', font=('Comic Sens', 12), width=15,command=set_reminder)
set_btn.pack(pady=10, padx=50, ipady=5)

stop_btn = tk.Button(text='Stop sound', font=('Comic Sens', 12), width=15,command=stop_reminder)
stop_btn.pack(pady=10, padx=50,  ipady=5)

check_reminder()

root.mainloop()