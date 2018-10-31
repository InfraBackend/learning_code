# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
import xlwt
from io import BytesIO


class ExportExcel:
    fmts = [
        '#,##0.00'
        'M/D/YY',
        'D-MMM-YY',
        'D-MMM',
        'MMM-YY',
        'h:mm AM/PM',
        'h:mm:ss AM/PM',
        'h:mm',
        'h:mm:ss',
        'M/D/YY h:mm',
        'mm:ss',
        '[h]:mm:ss',
        'mm:ss.0',
    ]

    def __init__(self, excel_name):
        """
        初始化
        :param excel_name: 表名
        """
        self.response = HttpResponse(content_type='application/vnd.ms-excel')
        self.response[
            'Content-Disposition'] = 'attachment;filename=' + excel_name + '.xls'
        self.wb = xlwt.Workbook(encoding='utf-8')

    def xxx(self, head_list, sheet_name='PRD'):
        """
        形成表头
        :param head_list: 表头数据
        :return:
        """
        sheet_prd = self.wb.add_sheet(sheet_name)  #
        style_heading = xlwt.easyxf('font: bold on; align:wrap on, vert centre, horiz center')
        style_body = xlwt.easyxf()
        j = 0
        for i in head_list:
            sheet_prd.write(0, j, i, style_heading)
            j += 1

        return {'sheet_prd': sheet_prd, 'style_body': style_body}

    def x(self):
        """
        导出
        :return:
        """
        output = BytesIO()
        self.wb.save(output)
        output.seek(0)
        self.response.write(output.getvalue())
        return self.response
