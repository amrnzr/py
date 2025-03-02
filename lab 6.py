#Python Directories and Files exercises
import os
import shutil
import string
 
#Task 1
def list_dir_files(path):
    print(f"Directories in '{path}':")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(item)

    print(f"\nFiles in '{path}':")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            print(item)

    print(f"\nAll in '{path}':")
    for item in os.listdir(path):
        print(item)

path = input()
print(list_dir_files(path))

#Task 2
def access(path):
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")
path = input()
print(access(path))

#Task 3
def exists(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print(f"Path '{path}' does not exist.")
path = input()
print(exists(path))

#Task 4
def lines(file):
    with open(file, 'r') as f:
        return sum(1 for line in f)
file = 'test.txt'
print(lines(file))

#Task 5
def list_to_file(file, lst):
    with open(file, 'w') as f:
        for item in lst:
                f.write(str(item) + '\n')
file = 'test.txt'
lst = ["pepsi", "soda", "laptop"]
print(list_to_file(file, lst))

#Task 6
def generate():
    for letter in string.ascii_uppercase:
        open(f"{letter}.txt", 'w').close()
print(generate())

#Task 7
def copy(one, two):
    shutil.copy(one, two)

def copy(one, two):
    with open(one, 'r') as fone, open(two, 'w') as ftwo:
        ftwo.write(fone.read())

one = 'test.txt'
two = 'text.txt'
print(copy(one, two))

#Task 8
def delete(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
    return "File not found or cannot be deleted"
path = input()
print(delete(path))


#Python builtin functions exercises
#Task 1
def multiply(n):
    return eval('*'.join(map(str, n)))

#Task 2
def count(s):
    a = sum(c.isupper() for c in s)
    b = sum(c.islower() for c in s)
    return f"upper: {a}, lower: {b}"

#Task 3
def palindrome(s):
    processed_s = ''.join(c.lower() for c in s if c.isalnum())
    return list(processed_s) == list(reversed(processed_s))

#Task 4
import time
def square_root_after_delay(number, delay):
    time.sleep(delay / 1000.0)
    result = number ** 0.5
    return result
number = int(input())
delay = int(input())
print(square_root_after_delay(number, delay))

#Task 5
def all_true(tup):
    return all(tup)
