import os
import tkinter as tk

from tkinter import ttk

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
        for F in (First, Second, Table):
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
        btn_1 = tk.Button(self, text="Перейти в следующий класс", command=lambda: controller.show_frame(Second))
        btn_1.pack()
        btn_2 = tk.Button(self, text="Перейти в класс отображения таблицы",
                          command=lambda: controller.show_frame(Table))
        btn_2.pack()


class Second(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = tk.Label(self, text=f"Это {__class__.__name__} класс")
        lbl.pack()
        btn = tk.Button(self, text="Вернуться в предыдущий класс", command=lambda: controller.show_frame(First))
        btn.pack()


class Table(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def set_table():
            from excel.modules.function import initial_data
            try:
                result = initial_data()
                columns = []
                for column in result:
                    columns.append(column)
                values = result.values

                Treeview = ttk.Treeview(self, columns=columns, show="headings")

                Treeview.heading("Проверка 1", text="Проверка 1")
                Treeview.heading("Проверка 2", text="Проверка 2")

                for value in values:
                    for i in value:
                        Treeview.insert("", tk.END, values=i)

                Treeview.pack()
            except Exception as ex:
                showerror("Даные не могут быть загружены", ex)

        btn = tk.Button(self, text="Выгрузить данные", command=set_table)
        btn.pack()
