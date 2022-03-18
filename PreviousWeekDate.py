from datetime import date
from datetime import timedelta


def previous_date():

    today = date.today()
    print(today)
    for i in range(7,84,7):
        d = today - timedelta(days=i)
        print(d)