# Ex 02 - getting an integer number and printing a triangle and parallelogram
# with the height of that number.

# getting the size from the user.
size = int(input("Insert size: "))
# running the loop "size" times to print the triangle and parallelogram.
for i in range(1, size + 1):
    # declaring the left space(left to the triangle).
    left_space = " " * (size - i)
    # declaring the triangle with base of (size * 2 - 1).
    triangle = "*" * (i * 2 - 1)
    # declaring the middle space between the triangle and the parallelogram.
    middle_space = " " * ((size - i) * 2)
    # declaring the parallelogram.
    parallelogram = "*" * size
    # printing all variables together as a single string.
    print(left_space + triangle + middle_space + parallelogram)
