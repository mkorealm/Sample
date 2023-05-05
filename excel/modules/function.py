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
