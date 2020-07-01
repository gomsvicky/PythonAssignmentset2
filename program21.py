import math
import random
n = 0.543

print("******Print All functions in math******")
n1 = round(n)
print("Rounding off number 0.543 :", n1)
print("math Square root of 144 : ", math.sqrt(144))
print("math ceil operation : ", math.ceil(20.456))
print("math factorial : ", math.factorial(5))
print("math remainder: ", math.remainder(15, 20))
print("math exponencial  : ", math.exp(2))
print("math finite : ", math.isfinite(100))
print("****Print All Random Functions********")
n3 = int(random.random())
print("Printing a random value :", n3)
n4 = int(random.uniform(10, 500))
print("Printing a uniform value between 10 and 500 :", n4)
print("Explore all functions in random")
num = 1000
n5 = random.randint(10, 500)
print("random int :", n5)
n6 = random.random()
print("random :", n6)
numbers = [1, 2, 3, 4, 5, 6]
n7 = random.shuffle(numbers)
print("shuffle :", numbers)
n8 = random.choice(numbers)
print("choice : ", n8)
n9 = random.randrange(10, 500)
print("Random range", n9)