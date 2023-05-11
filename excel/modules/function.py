def insert_zapis(lst: list):
    from tkinter.messagebox import showerror
    import pandas

    from gui.main import script_dir

    result = pandas.DataFrame({"Данные": [*lst]})
    try:
        writer = pandas.ExcelWriter(script_dir + "\\Insert.xlsx", engine='xlsxwriter')
        result.to_excel(writer, sheet_name='Страница 1')
        writer.close()
    except Exception as ex:
        showerror("Ошибка", ex)


def initial_data():
    from tkinter.messagebox import showerror
    import pandas

    from gui.main import script_dir

    try:
        xl = pandas.ExcelFile(script_dir + "\\..\\Initial.xlsx")
        result = xl.parse(xl.sheet_names[0])
        return result
    except Exception as ex:
        showerror("Ошибка", ex)
