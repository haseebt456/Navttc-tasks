# Python program to fint the area of a triangle
a = float(input("Enter first side of triangle: "))
b = float(input("Enter second side of triangle: "))
c = float(input("Enter third side of triangle: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)