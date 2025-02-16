list = [x for x in range(1, 6) if x % 2 == 1]
ourtuple = ("bmw", "m5", 1995, "black")
make, model, year, color = ourtuple
def func(num1 = 1, num2 = 0):
    print(num1 + num2)

func(3, 5)
func("hello ", "all")
func ([1, 2, 3], [4, 5, 6])

def func(*args):
    print(args)
    for arg in args:
        print(arg)
func(1, 2, 3, "messi")

class Person:
    name = "Messi"
    age = 19
    person = Person()
    print(type(person))
    print(person.name)
    print(person.age)

#it
a = [1, 2, 3]
aiter = iter(a)
print(next(aiter)) #1
print(next(aiter)) #2