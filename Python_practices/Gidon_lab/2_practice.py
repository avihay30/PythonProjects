# lab 2: 1-
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# y = a*2+b**2+c
# print("y=a*2+b**2+c=%d*2+%d**2+%d=%d" %(a, b, c, y))

# 2-
# edge = float(input("Enter edge of triangle: "))
# height = float(input("Enter height of triangle: "))
# area = (edge*height)/2
# print("The area is:", "%.3f" % area)

# 3-
# price = float(input("Enter price, please: "))
# discount = 0.85
# print("Price after discaount: ", "%.2f" % (price*discount))

# 4- first way:
# number = int(input("Enter number: "))
# seperator = "%-13d%-13d%-13d"
# print("Number", "Square", "Cube", sep = "       ")
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))

# 4- second way:
# number = int(input("Enter number: "))
# seperator = "%3d%14d%14d"
# print("Number", "Square", "Cube", sep = "       ")
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))
# number = number + 1
# print(seperator % (number, number**2, number**3))

# practice

dollars = int(input("Enter the moeny: ")) 
twenies = dollars//20
tens = (dollars-twenies*20)//10
fives = (dollars-twenies*20-tens*10)//5
ones = (dollars-twenies*20-tens*10-fives*5)

print("twenies: %d, tens: %d, fives: %d, ones: %d" %(twenies, tens, fives, ones))