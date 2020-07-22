import openpyxl

wb = openpyxl.load_workbook("excelfile.xlsx")
print(wb.sheetnames)

active_sheet = wb['excelfile']
print(active_sheet['B5'].value)
print(list(active_sheet.columns))

for i in list(active_sheet.rows):
    for j in i:
        print(j.value)

