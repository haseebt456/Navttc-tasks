from numpy import random
print("Random integer from 0 to 100:")
x = random.randint(100)

print(x)
print("Random float from 0 to 1:")
x = random.rand()

print(x)
print("list of Random integer from 0 to 100 with size of 5:")
x=random.randint(100, size=(5))

print(x)
print("2-d array of Random integer from 0 to 100 with size of 3x5:")
x = random.randint(100, size=(3, 5))
print("2-d array of Random integer from 0 to 100 with size of 3x5:")

print(x)
print("1-d array of Random float from 0 to 1 with size of 5:")
x = random.rand(5)

print(x)
print("2-d array of Random float from 0 to 1 with size of 3x5:")
x = random.rand(3, 5)

print(x)
print("Random choice from array [3, 5, 7, 9]:")
x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)
