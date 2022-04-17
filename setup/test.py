# from tkinter import *

# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = Frame(self.master)
#         self.button1 = Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.grid(column=0, row=0)
#         self.frame.grid(column=0, row=0)

#     def new_window(self):
#         self.newWindow = Toplevel(self.master)
#         self.app = Demo2(self.newWindow)

# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = Frame(self.master)
#         self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.grid(column=0, row=0)
#         self.frame.grid(column=0, row=0)

#     def close_windows(self):
#         self.master.destroy()

# def main(): 
#     root = Tk()
#     app = Demo1(root)
#     root.mainloop()

# if __name__ == '__main__':
#     main()

from calendar import month
from pydoc import TextRepr
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import Calendar, DateEntry

global date
top = Tk()

ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

style = ttk.Style()
style.theme_use('clam')  # -> uncomment this line if the styling does not work
dateentry = DateEntry(top, width=12, selectmode='day', borderwidth=2)
dateentry.config(year=2019, day=10, month=12)
def dateentry_used(*args):
    date = dateentry.get_date()
    print(date)
dateentry.bind("<<DateEntrySelected>>", dateentry_used)
dateentry.pack(padx=10, pady=10)


top.mainloop()
