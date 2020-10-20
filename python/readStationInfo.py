# coding=utf-8
# MEB立库根据点位读取路径

import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(5)

    for rowNum in range(table.nrows):
        rowVale1 = table.row_values(1)
        rowVale = table.row_values(rowNum)
        for colNum in range(table.ncols):
            if rowVale[colNum]=='●':
                print(rowVale[1] +' ' + rowVale1[colNum])

    # if判断是将 id 进行格式化
    # print("未格式化Id的数据：")
    # print(table.cell(1, 0))
    # 结果：number:1001.0


if __name__ == '__main__':
    excelFile = 'D:/repos/AnjiGit/meb-cube-wms/doc/C.系统设计/04.软件规格/设计文档20200608.xlsx'
    read_xlrd(excelFile=excelFile)