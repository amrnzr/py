#Python Classes
#Task 1
class String:
    def __init__(self):
        pass
    def getString(self):
        self.text = input()
    def printString(self):
        print(self.text.upper())

#Task 2
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

#Task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

#Task 4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point({self.x}, {self.y})")
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
#Task 5
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")

#Task 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True
numbers = list(range(1, 20))
primes = list(filter(lambda x: is_prime(x), numbers))
print(primes)


#Python Function 1
#Task 1
def g_to_o(grams):
    return grams * 28.3495231
grams = float(input())
ounces = g_to_o(grams)
print(f"{grams} grams is equal to {ounces:.2f} ounces")

#Task 2
def f_to_c(F):
    return (5 / 9) * (F - 32)
F = input()
C = f_to_c(F)
print(f"{F} Fahrenheit is equal to {C:.2f} Centigrade")

#Task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "Impossible"
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"chickens: {chickens}, rabbits: {rabbits}")

#Task 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return list(filter(is_prime, numbers))
numbers = [int(x) for x in input().split()]
print(filter_prime(numbers))

#Task 5
from itertools import permutations
def print_perms(s):
    perms = permutations(s)
    for perm in perms:
        print("".join(perm))
s = input()
print(print_perms(s))

#Task 6
def reverse(s):
    return " ".join(s.split()[::-1])
s = input()
print(reverse(s))

#Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums = [int(x) for x in input().split()]
print(has_33(nums))

#Task 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
            if not code:
                return True
    return False
nums = [int(x) for x in input().split()]
print(spy_game(nums))

#Task 9
def sphere_vol(radius):
    return 4 / 3 * 3.14 * (radius ** 3)
radius = int(input())
print(sphere_vol(radius))

#Task 10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
lst = list(input())
print(unique_elements(lst))

#Task 11
import re
def is_pal(s):
    clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return clean == clean[::-1]
s = input()
print(is_pal(s))

#Task 12
def histogram(nums):
    for n in nums:
        print('*' * n)
nums = [int(x) for x in input().split()]
histogram(nums)

#Task 13
import random
def guess():
    num = random.randint(1, 20)
    attempts = 0
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess")
    while True:
        try:
            n = int(input())
            attempts += 1
            if n < num:
                print("Your guess is too low.\nTake a guess.")
            elif n > num:
                print("Your guess is too big.\nTake a guess.")
            else:
                print(f"Good job, KBTU! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")
game = guess()
print(game)


#Python Function 2
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Task 1
def high_rated_movie(movie):
    return movie["imdb"] > 5.5
movie = movies[3]
print(high_rated_movie(movie))

#Task 2
def high_rated_movies(movies):
    return [movie for movie in movies if high_rated_movie(movie)]
print(high_rated_movies(movies))

#Task 3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]
category = "Suspense"
print(movies_by_category(movies, category))

#Task 4
def av_imdb_score(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)
print(av_imdb_score(movies))

#Task 5
def av_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return av_imdb_score(category_movies)
print(av_imdb_score_by_category(movies, "Thriller"))
