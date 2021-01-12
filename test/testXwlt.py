import xlwt

# 创建workbook
workbook = xlwt.Workbook(encoding='utf-8')
# 创建worksheet
worksheet = workbook.add_sheet('sheet1')

# 在第一行第一列写入hello
worksheet.write(0, 0, 'hello')

# 保存数据表
workbook.save('student.xls')
