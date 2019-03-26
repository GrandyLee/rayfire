import xlrd
import xlwt


file = '电子驾照.xlsx'
data = xlrd.open_workbook(file)

sheet_names = data.sheet_names()  # 获取excel所有sheet标签的名字
print(sheet_names)
print(sheet_names[0])
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_name('测试用例')
sheet3 = data.sheet_by_name('人员')
print(sheet1)
print(sheet2)
print(sheet3)

rows = sheet3.nrows
print(rows)
cols = sheet3.ncols
print(cols)

row_data_1 = sheet3.row_values(0)
row_data_2 = sheet3.row_values(1)
col_data_1 = sheet3.col_values(0)

print(row_data_1)
print(row_data_2)
print(col_data_1)

for t in range(1, rows):
    row_value = sheet3.row_values(t)
    print(row_value)


# result = xlwt.Workbook(encoding='ascii')
# worksheet = result.add_sheet('test_result')
# worksheet.write(0, 0, 'this is test')
# result.save('result.xls')
