# import array
# # print(x[:5])
# # del x[:5]
# # print(x)
#
# import xlsxwriter
# workbok = xlsxwriter.Workbook("output.xlsx")
# sheet = workbok.add_worksheet()
# i=0
# x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#
#
# for item in range(len(x)):
#     sheet.write(item, 0, x[item])
#
#
# # x1=[]
# # while i <= len(x):
# #     x1= (x[:5])
# #     print(x1)
# #     for k in range(len(x1)):
# #         sheet.write(i, k, x[k])
# #         k=+1
# #
# #     del x1[:]
# #     del x[:5]
# #     i=+1

import xlsxwriter

workbook  = xlsxwriter.Workbook('wow.xlsx')
worksheet = workbook.add_worksheet()

# worksheet.write(0, 0, 'Hello Excel')
i=0
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
x1=[]
while i <= len(x):
    x1= (x[:5])
    print(x1)
    for k in range(len(x1)):
        worksheet.write(i+3, k, x[k])
    del x1[:]
    del x[:5]
    i=+1

workbook.close()