import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import datetime 
import time
import pygame
import os
import sys

# Инициализация глобальных переменных
t_stamp = 0  # Временная метка для напоминания
music = False  # Флаг для воспроизведения музыки
reminder_text = ""  # Текст напоминания

def set_reminder():
    global t_stamp, reminder_text
    # Запрос времени напоминания у пользователя
    remind = simpledialog.askstring('Reminder time', 'Enter reminder\n(in 24 hour)', initialvalue="HH:MM", parent=root)
    if remind:
        # Удаление всех символов, кроме цифр
        time_str = remind.replace(' ', '').replace(':', '').replace('.', '').replace('-', '').replace('/', '')
        if len(time_str) == 4 and time_str.isdigit():
            # Преобразование введённого времени в часы и минуты
            hour = int(time_str[:2])
            minute = int(time_str[2:])
            now = datetime.datetime.now()
            # Создание объекта datetime для времени напоминания
            time_rem = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            # Если время напоминания уже прошло, добавляем один день
            if time_rem <= now:
                time_rem += datetime.timedelta(days=1)  
            t_stamp = time_rem.timestamp()
            # Запрос текста напоминания у пользователя
            text = simpledialog.askstring('Reminder text',  'Please enter reminder text: ', initialvalue='Reminder text', parent=root)
            if text:
                reminder_text = text
                # Обновление текста метки с информацией о напоминании
                lbl.config(text=f'Reminder set \n{time_rem.strftime("%H:%M")}\n "{text}"')
            else:
                lbl.config(text=f'Reminder set \n{time_rem.strftime("%H:%M")}')
        else:
            # Вывод сообщения об ошибке при неверном формате времени
            messagebox.showerror('Error', 'Invalid time format. Please enter HHMM or HH:MM.')
    else:
        messagebox.showerror('Error', 'Invalid time format. Please enter HH:MM.')

def check_reminder():
    global t_stamp
    if t_stamp:
        now = time.time()
        # Проверка, наступило ли время напоминания
        if now >= t_stamp:
            play_sound()
            # Вывод сообщения с текстом напоминания
            show_custom_messagebox()
            t_stamp = None
    # Повторная проверка через 10 секунд
    root.after(10000, check_reminder)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def play_sound():
    global music
    music = True
    try:
    # Инициализация модуля pygame для воспроизведения звука
        pygame.mixer.init()
        # Загрузка и воспроизведение музыкального файла
        pygame.mixer.music.load(resource_path('./music/Ariis - Funk Do Bounce.mp3'))
        pygame.mixer.music.play(loops=3)
    except pygame.error as e:
        messagebox.showerror('Error', f'Failed to play sound: {e}')
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred: {e}')

def stop_reminder():
    global music
    if music:
        # Остановка воспроизведения музыки
        pygame.mixer.music.stop()
        music = False
    # Обновление текста метки
    lbl.config(text='Add new Reminder')

def show_custom_messagebox():
    # Создание нового окна
    top = tk.Toplevel(root, bg='lightgreen')
    top.title('Your Reminder')
    top.attributes('-topmost', True, '-alpha', 0.7)  # Установка окна поверх всех других
    top.focus_set()
    # Создание метки с текстом напоминания
    label = tk.Label(top, text=reminder_text, bg='lightgreen', bd=2,  font=('Arial', 12, 'bold'))
    label.pack(padx=20, pady=20)

    # Создание кнопки для закрытия окна
    ok_button = tk.Button(top, text='OK', bg='#00d700',  activebackground='#008040', 	activeforeground='#ffffcc',  font=('Comic Sens MS', 12, 'bold'), width=15, command=top.destroy)
    ok_button.pack(side=tk.LEFT, pady=10, padx=50, ipady=5)
    stop_btn = tk.Button(top, text='Stop sound', bg='#00d700',  activebackground='#008040', 	activeforeground='#ffffcc', font=('Comic Sens MS', 12, 'bold'), width=15, command=stop_reminder)
    stop_btn.pack(side=tk.LEFT, pady=10, padx=50, ipady=5)
   

# Создание главного окна приложения
root = tk.Tk()
root.title('Reminder')
# root.withdraw()  

# Центрирование окна на экране
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.update_idletasks() 

# Создание и размещение метки с текстом
lbl = tk.Label(text='Add Reminder', font=('Comic Sens MS', 16))
lbl.pack(pady=10)

# Создание и размещение кнопки для установки напоминания
set_btn = tk.Button(text='Set Reminder', font=('Comic Sens MS', 12), width=15, command=set_reminder)
set_btn.pack(pady=10, padx=50, ipady=5)

# Создание и размещение кнопки для остановки звука
# stop_btn = tk.Button(text='Stop sound', font=('Comic Sens MS', 12), width=15, command=stop_reminder)
# stop_btn.pack(pady=10, padx=50, ipady=5)

# Запуск цикла проверки напоминаний
check_reminder()

# Запуск основного цикла событий Tkinter
root.mainloop()