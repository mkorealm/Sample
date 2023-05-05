import os
import tkinter as tk


def select_table(file):
    import openpyxl
    columns = []  # return
    values = []  # return
    try:
        wb = openpyxl.load_workbook(filename=file)
        column = wb.worksheets[0]
        for row in column:
            values.append(row[0].value)
            columns.append(row[1].value)
    except Exception as ex:
        showerror("Ошибка!", str(ex))


script_dir = os.path.dirname(__file__)

try:
    from tkinter.messagebox import showerror
    from database.connect.connect import Connect
    from database.connect.config import db

    connect = Connect(*db)
except Exception as ex:
    showerror("Ошибка подключения к серверу", ex)


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Королев Максим 41ИС-19")

        container = tk.Frame(self, pady=150, padx=200)
        container.pack()

        self.frames = {}
        for F in (First, Second):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame(First)

    def show_frame(self, content):
        frame = self.frames[content]
        frame.tkraise()


class First(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = tk.Label(self, text=f"Это {__class__.__name__} класс")
        lbl.pack()
        btn = tk.Button(self, text="Перейти в следующий класс", command=lambda: controller.show_frame(Second))
        btn.pack()


class Second(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = tk.Label(self, text=f"Это {__class__.__name__} класс")
        lbl.pack()
        btn = tk.Button(self, text="Вернуться в предыдущий класс", command=lambda: controller.show_frame(First))
        btn.pack()
