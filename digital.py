# def int_format(i, n=None):
#     """
#
#     """
#     r = i / 10000
#     ret = round(r, n)
#     return ret
#
# print(int_format(33))
from dateutil.relativedelta import relativedelta
import calendar, datetime

def get_vintage():
    # vintages = get_vintages(channel_id, province_id)
    mob_rate_list = []
    today = datetime.date.today()
    n = today.month
    i = 1
    while i <= n:
        mob_dict = {}

        # two_year_ago = today - relativedelta(months=n)
        str_year_month = i
        # firstDayWeekDay, monthRange = calendar.monthrange(today.year,
        #                                                   today.month)
        # str_two_year_ago = '%s-%s' % (str_year_month, monthRang/e)
        # vintage = vintages.filter(loan_date=str_two_year_ago).aggregate(
        #     mob_rate=Sum(mob), contract_amount=Sum('contract_amount')
        # )
        mob_dict['months'] = str_year_month
        # if vintage['contract_amount'] is not None and vintage[
        #     'mob_rate'] is not None and vintage[
        #     'contract_amount'] != 0:
        #     mob_dict['values'] = utils.float_format(
        #         vintage['mob_rate'] / vintage['contract_amount'], 4)
        # else:
        mob_dict['values'] = None
        mob_rate_list.append(mob_dict)
        i += 1
    return mob_rate_list

print(get_vintage())