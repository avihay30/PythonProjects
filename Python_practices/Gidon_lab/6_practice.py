# 1-
def func1(a, b):
    a += 2
    b -= 3
    x = a + b
    print(a, b, x, y)
    return x


def func2():
    global a, b
    a **= 2
    b += a
    print(a, b)


a, b = 3, 4
x, y = 10, 0
print(a, b, x, y)
y = func1(a, b)
print(a, b, x, y)
func2()
print(a, b)


# 2-
# declaring "printing_triangle" that gets a char and a number and printing the
# (char * number) in x(number) rows.
def printing_triangle(char, number):
    # running the first loop that create the rows.
    for i in range(number):
        # running the second loop to print the "char" "number" times in the
        # same row[i]
        for j in range(number - i):
            # printing the char every iteration and space afterwords.
            print(char, end=" ")
        # printing new empty row.
        print()


# getting a letter from the user.
letter = input("Enter a letter: ")
# getting a integer number from the user.
n = int(input("Enter an integer: "))

# printing a title before printing the triangle.
print("*** Triangle ***")
# calling to the function with the user values.
printing_triangle(letter, n)

# 3-
# importing a library named "math"
import math


# declaring "height" function that gets a (velocity, angle, time) and returning
# the height according to the arguments(velocity, angle, time).
def height(velocity, angle, time):
    # declaring an gravity variable with the value of 9.81
    gravity = 9.81
    # calculating the velocity of y axis(using the lib "math" and "deg2rad"
    # function) and saving him in a variable.
    vy = velocity * math.sin(deg2rad(angle))
    # calculating the height according to the vy and the time and gravity.
    h = vy * time - gravity * time ** 2 / 2
    # returning the height.
    return h


# declaring "horizontal" function that gets a (velocity, angle, time) and
# returning the horizontal distance.
def horizontal(velocity, angle, time):
    # calculating the velocity of x axis(using the lib "math" and "deg2rad"
    # function) and saving him in a variable.
    vx = velocity * math.cos(deg2rad(angle))
    # calculating the horizontal distance according to the vx and the time. 
    s = vx * time
    # returning the horizontal distance.
    return s


# declaring "deg2rad" function the gets an angle and returning
# the angle in radians.
def deg2rad(angle):
    return math.radians(angle)


# running an endless loop.
while True:
    # getting the velocity and angle from the user.
    v, a = eval(input("Enter v(0-100) m/s and a(0-90 degrees): "))
    # checking if the input is invalid.
    if (v > 100 or v < 0) or (a < 0 or a > 90):
        # printing "Finish".
        print("Finish!")
        # stopping the main loop.
        break

    # declaring a variable named "t" and initial it with the value of 0.1.
    t = 0.1
    # declaring a variable named "h" and initial it with first calculation
    # of the height(with the function "height").
    h = height(v, a, t)
    # running a loop until the height is less or equal to 0.
    while h >= 0:
        # declaring a variable named "s" with the returned value of
        # "horizontal" function.
        s = horizontal(v, a, t)
        # declaring a variable named "h" with the returned value of
        # "height" function.
        h = height(v, a, t)
        # printing the current time, horizontal distance and height.
        print("Time: %.1f... S = %.2f H = %.2f" % (t, s, h))
        # incrementing the time with 0.1.
        t += 0.1
    # when the second loop is ended printing "Fallen".
    print("Fallen!")
