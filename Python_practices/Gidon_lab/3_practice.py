# 1-
# getting input parameter x from the user
x = float(input("Enter x: "))
# calculating the equation(x + sqrt(x^(1/3)+x^2))
result = x + (x ** (1 / 3) + x ** 2) ** 0.5
# printing the equation
print("%s+sqrt(%s^(1/3)+%s^2) = %.2f" % (x, x, x, result))

# # 2-
# # getting 3 edges of a triangle from the user
# a, b, c = eval(input("Enter a,b,c: "))
# # calculating the perimeter according to the input
# perimeter = a + b + c
# # creating a half of the perimeter variable
# # to make the "Heron's formula" more readable
# p = perimeter / 2
# # calculating the area according to "Heron's formula"
# area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# # printing the 3 edges
# print("The edges are: a=%d, b=%d, c=%d" % (a, b, c))
# # printing the perimeter
# print("The perimeter is: %.3f" % perimeter)
# # printing the area
# print("The area is: %.3f" % area)
#
# # 3-
# # getting 2 perpendicular of a triangle from the user
# a, b = eval(input("Enter a,b: "))
# # calculating the hypotenuse of the triangle using Pythagoras formula
# c = (a ** 2 + b ** 2) ** 0.5
# # calculating the perimeter according to a,b,c
# perimeter = a + b + c
# # calculating the area according to the fact it's a right triangle.
# area = a * b / 2
#
# # printing the perimeter
# print("The perimeter is: %.3f" % perimeter)
# # printing the area
# print("The area is: %.3f" % area)
#
# # # 4-
# # # getting the area of a right and isosceles triangle from the user
# # area = float(input("Enter the area of the triangle: "))
# # # calculating the 2 edges according to the fact its right and isosceles triangle
# # # it's possible to not save it in different variables, I did so for readability.
# # a = b = (area * 2) ** 0.5
# # # calculating the hypotenuse of the triangle using Pythagoras formula
# # c = (a ** 2 + b ** 2) ** 0.5
# #
# # # printing the result of the 3 edges of the triangle
# # print("Sides of the triangle are: a=%.2f, b=%.2f, c=%.2f" % (a, b, c))
#
# # calculating and printing the results of quad formula
# # (-b +-  (b**2 - 4 * a * c)**0.5) / 2*a
# # a, b, c = eval(input("Enter the three values: "))
# # sqrt_result = b**2 - 4*a*c
# # if sqrt_result < 0:
# #    print("there is no real solutions")
# # elif sqrt_result == 0:
# #    print("There is one solution: x=%.2f" %(-b/(2*a)))
# # else:
# #    first_solution = (-b + sqrt_result**0.5) / (2*a)
# #    second_solution = (-b - sqrt_result**0.5) / (2*a)
# #    print("There is two solutions: x1=%.2f, x2=%.2f" %(first_solution, second_solution))
