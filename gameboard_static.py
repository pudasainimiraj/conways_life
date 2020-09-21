import tkinter as tk
from game import Game

class Conway(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def write(self):
        print(game().getName)

root=tk.Tk()
app=Conway(master=root)
app.mainloop()
