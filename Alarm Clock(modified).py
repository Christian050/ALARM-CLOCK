from datetime import datetime
from tkinter import *
from time import strftime
from playsound import playsound


class CreateAlarm:
    def __init__(self, master):
        self.master = master
        self.background = 'Black'
        self.foreground = 'White'
        self.master.title('Alarm Clock')
        self.master.config(bg=self.background)
        self.master.resizable(0, 0)
        self.time = StringVar()
        self.date = StringVar()
        self.alarmTime = None
        self.font = ('Calibri', 30, 'bold')

        Label(self.master, text='Time', bg=self.background,
              fg=self.foreground).pack(anchor='center')
        Label(self.master, textvariable=self.time, font=self.font,
              bg=self.background, fg=self.foreground).pack(anchor='center')

        Label(self.master, text='Date', bg=self.background,
              fg=self.foreground).pack(anchor='center')
        Label(self.master, textvariable=self.date, font=self.font,
              bg=self.background, fg=self.foreground).pack(anchor='center')

        Button(self.master, text='Set Alarm', command=self.popup).pack()

        self.update()
        self.master.mainloop()

    def update(self):
        now = datetime.now()
        time = strftime('%H:%M:%S')
        date = strftime('%d/%m/%y ')
        self.time.set(time)
        self.date.set(date)
        if self.alarmTime is not None and now.strftime('%H:%M:%S') == self.alarmTime:
            playsound('Ringtone\iphone_alarm.mp3')
            self.alarmTime = None
            
        self.master.after(1000, self.update)

    def popup(self):
        win = Toplevel(self.master)
        win.title('Alarm Clock')
        win.resizable(0, 0)
        win.config(bg=self.background)

        LF = LabelFrame(win, text='Set Alarm', bg=self.background, fg=self.foreground)
        LF.pack(padx=5,pady=5, ipadx=15, ipady=10)

        HF = LabelFrame(LF, text='Hour', bg=self.background, fg=self.foreground, bd=0)
        HF.grid(row=0, column=1, padx=10)

        Hour = Entry(HF, width=8, justify='center', bg=self.foreground)
        Hour.pack(pady=5, padx=5)

        MF = LabelFrame(LF, text='Minute', bg=self.background, fg=self.foreground, bd=0)
        MF.grid(row=0, column=2, padx=10)

        Minute = Entry(MF, width=8, justify='center', bg=self.foreground)
        Minute.pack(pady=5, padx=5)

        SF = LabelFrame(LF, text='Second', bg=self.background, fg=self.foreground, bd=0)
        SF.grid(row=0, column=3)

        Second = Entry(SF, width=8, justify='center', bg=self.foreground)
        Second.grid(pady=5, padx=5)
        
        Button(LF, text='Set Alarm', command=lambda: self.setAlarm(Hour, Minute, Second, win)).grid(row=1, column=2)

    def setAlarm(self, Hour, Minute, Second, win):
        hour = Hour.get()
        minute = Minute.get()
        second = Second.get()

        if hour.isdigit() and minute.isdigit() and second.isdigit():
            self.alarmTime = f"{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}"
            win.destroy()

root = Tk()
app = CreateAlarm(root)
