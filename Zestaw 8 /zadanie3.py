import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar  # pip install tkcalendar

okno = tk.Tk()
# tytuł, rozmiar, blokada wielkości
okno.title("Calendar")
okno.geometry("400x350")
okno.resizable(False, False)
# utwórz StringVar()
date_time = StringVar()

def update_date_time():
	day = datetime.today().strftime('%A')
	date = datetime.today().strftime('%d')
	month = datetime.today().strftime('%B')
	year = datetime.today().strftime('%Y')
	time = datetime.today().strftime('%H:%M:%S')
	dt = day + ", " + date + " " + month + " " + year + "\n" + time
	date_time.set(dt)
	okno.after(1000, update_date_time)


date_time_label = Label(okno, textvariable = date_time, font = ("Calibri", 25), bg = 'black', fg = 'white', width = 500, pady = 40)
date_time_label.pack(anchor="center")
current_time = datetime.now()
day = int(current_time.strftime('%d'))
month = int(current_time.strftime('%m'))
year = int(current_time.strftime('%Y'))
calendar = Calendar(okno, font = ("Arial", 12), selectmode = 'day', year = year, month = month, day = day)
calendar.pack(anchor = "center", pady = 10)


update_date_time()

okno.mainloop()