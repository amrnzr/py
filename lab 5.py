#Python RegEx exercises
import re
#Task 1
def a_and_b(s):
    return bool(re.fullmatch(r'ab*', s))
s = str(input())
print(a_and_b(s))
#Task 2
def twob(s):
    return bool(re.fullmatch(r'ab{2,3}', s))
s = str(input())
print(twob(s))
#Task 3
def low(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)
s = str(input())
print(low(s))
#Task 4
def up_and_low(s):
    return re.findall(r'[A-Z][a-z]+', s)
s = str(input())
print(up_and_low(s))
#Task 5
def a_to_b(s):
    return bool(re.fullmatch(r'a.*b', s))
s = str(input())
print(a_to_b(s))
#Task 6
def colon(s):
    return re.sub(r'[ ,.]', ':', s)
s = str(input())
print(colon(s))
#Task 7
def sn_to_cam(s):
    return ''.join(word.capitalize() for word in s.split('_'))
s = str(input())
print(sn_to_cam(s))
#Task 8
def split_up(s):
    return re.split(r'(?=[A-Z])', s)
s = str(input())
print(split_up(s))
#Task 9
def ins_space(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
s = str(input())
print(ins_space(s))
#Task 10
def cam_to_sn(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
s = str(input())
print(cam_to_sn(s))