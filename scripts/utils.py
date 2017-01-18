from datetime import datetime
import calendar
import dateutil
import sys

cal = calendar.Calendar()
cal.setfirstweekday(calendar.SUNDAY)

def week_of_month(date):
    """
    return the week of a month for a given date acconding google search query API works
    """
    weeks = cal.monthdayscalendar(date.year, date.month)
    for week in weeks:
        if date.day in week:
            if week[0] > 0:
                return '{}.{}.{}'.format(week[0], date.month, date.year)
            else:
                month = (date.month - 1) if calendar.month_name[date.month] != 'January' else 12
                year = date.year if calendar.month_name[date.month] != 'January' else (date.year - 1)
                last = cal.monthdayscalendar(year, month)
                return '{}.{}.{}'.format(last[-1][0], month, year)
