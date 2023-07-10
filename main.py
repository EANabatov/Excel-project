import xlsxwriter


workbook = xlsxwriter.Workbook('training_data/OMS.xlsx')
worksheet = workbook.add_worksheet()


workbook.close()