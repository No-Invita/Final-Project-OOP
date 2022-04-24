from tkinter import *
import tkinter  as tk
from PIL import Image,ImageTk
import time
import datetime
from datetime import date

main_window = Tk()
main_window.title('Peter Assistant')

main_window.geometry('360x640')
main_window.resizable(0,0)

bg = ImageTk.PhotoImage(Image.open('src/resources/peter.png'))
background = Label(main_window, image = bg)
background.pack()

class Digital_clock():
    def __init__(self):
    
        self.current_time_label = Label(text="", font=('Radioland', 16), bg='#0F0F0F', fg='aqua', pady=0, padx=0)
        self.week_day_label = Label(text="", font=('Radioland', 10),bg='#0C0A3B', fg='#B30F7B', pady=0, padx=0 )
        self.current_time_label.place(x=2, y=3)
        
        self.week_day_label.place(x=90, y=426)
        self.update_clock()
        self.get_date()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.current_time_label.configure(text=now)
        
        main_window.after(1000, self.update_clock)

    def get_date(self):
        # Get Week Day
        datetime_object = datetime.datetime.now()
        week_day = datetime_object.strftime("%A")

        # Get Current date
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        self.week_day_label.configure(text = d1 + '|' + week_day)


Prueba = Digital_clock()
main_window.mainloop()

