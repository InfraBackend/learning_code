# -*- coding: utf-8 -*-
import time

from .utils import ExportExcel
def export_capital_province(queryset):
    today = time.strftime('%Y%m%d%H%M%S')
    excel_name = '%s_province' % (today,)
    head_list = ['序号', '省市', '合同金额', '审批金额(不含退款)', '通过件数', '拒件数', '通过率',
                 '退件金额', '退件数'
                 ]
    export_excel = ExportExcel(excel_name)
    dct = export_excel.xxx(head_list)
    sheet_prd = dct['sheet_prd']
    style_body = dct['style_body']
    row = 1
    if queryset:
        for content in queryset:
            sheet_prd.write(row, 0, content.get('id'), style_body)
            sheet_prd.write(row, 1, content.get('province_name'), style_body)
            sheet_prd.write(row, 2, content.get('contract_amount__sum', 0), style_body)
            sheet_prd.write(row, 3, content.get('apply_amount_remove_refund__sum'), style_body)
            sheet_prd.write(row, 4, content.get('across_count__sum', 0), style_body)
            sheet_prd.write(row, 5, content.get('refuse_count__sum', 0), style_body)
            sheet_prd.write(row, 6, content.get('across_rate'), style_body)
            sheet_prd.write(row, 7, content.get('refund_amount__sum', 0), style_body)
            sheet_prd.write(row, 8, content.get('refund_count__sum', 0), style_body)
            row += 1
    return export_excel.x()