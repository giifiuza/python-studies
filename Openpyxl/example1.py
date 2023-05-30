from openpyxl import workbook, load_workbook

wb = load_workbook('teste.xlsx')
plan = wb.active
plan['A1'] = "Numero"

wb.save('teste.xlsx')