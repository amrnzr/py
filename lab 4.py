#Python date
from datetime import datetime, timedelta
#Task 1
def fivedays():
    return datetime.now() - timedelta(days=5)
#Task 2
def ytt():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday, today, tomorrow
#Task 3
def micro(dt):
    return dt.replace(microseconds=0)
#Task 4
def difference(date1, date2):
    return abs((date2 - date1).total_seconds())