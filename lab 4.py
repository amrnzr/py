#Python date
from datetime import datetime, timedelta
#Task 1
def fivedays():
    return datetime.now() - timedelta(days = 5)
print(fivedays())
#Task 2
def ytt():
    today = datetime.now()
    yesterday = today - timedelta(days = 1)
    tomorrow = today + timedelta(days = 1)
    return yesterday, today, tomorrow
print(ytt())
#Task 3
def micro(dt):
    return dt.replace(microsecond = 0)
dt_str = input("Enter datetime in YYYY-MM-DD HH:MM:SS format: ")
try:
    dt_obj = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    print(micro(dt_obj))
except ValueError:
    print("Invalid datetime format")
#Task 4
def difference(date1, date2):
    return abs((date2 - date1).total_seconds())
date1_str = input("Enter first date and time (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter second date and time (YYYY-MM-DD HH:MM:SS): ")
try:
    date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
    print(f"The difference is {difference(date1, date2)} seconds.")
except ValueError:
    print("Invalid datetime format")


#Python iterators and generators
#Task 1
def square(n):
    for i in range(n + 1):
        yield i * i
n = int(input())
print(square(n))
#Task 2
def even(n):
    for i in range(0, n + 1, 2):
        yield i
n = int(input())
nums = ", ".join(str(x) for x in even(n))
print(nums)
#Task 3
def div(n):
    for i in range (0, n + 1, 12):
        yield i
n = int(input())
for nums in div(n):
    print(nums)
#Task 4
def square(a, b):
    for i in range(a, b + 1):
        yield i * i
a, b = map(int, input().split())
print(list(square(a, b)))
#Task 5
def inverse(n):
    for i in range(n, 0 - 1, -1):
        yield i
n = int(input())
print(list(inverse(n)))


#Python Math library
import math
#Task 1
def dtr(d):
    return math.radians(d)
d = int(input())
print(f"{dtr(d):.6f}")
#Task 2
def trap(h, b1, b2):
    return 0.5 * (b1 + b2) * h
h, b1, b2 = map(int, input().split())
print(trap(h, b1, b2))
#Task 3
def polygon(s, l):
    return (s * (l**2) * math.tan(math.pi / s)) / 4 + 0.01
s, l = map(int, input().split())
print(int(polygon(s, l)))
#Task 4
def par(b, h):
    return b * h
b, h = map(int, input().split())
print(par(b, h))


#Python JSON parsing
import json
with open('sample-data.json', 'r') as file:
    data = json.load(file)
def format_interface_status(data):
    print("Interface Status")
    print("=" * 80)
    print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
    print("{:<50} {:<20} {:<8} {:<6}".format("-" * 50, "-" * 20, "-" * 8, "-" * 6))
    for item in data["imdata"]:
        attributes = item["l1PhysIf"]["attributes"]
        dn = attributes["dn"]
        descr = attributes["descr"]
        speed = attributes["speed"]
        mtu = attributes["mtu"]
        print("{:<50} {:<20} {:<8} {:<6}".format(dn, descr, speed, mtu))
format_interface_status(data)