# Ex 02 - getting an integer number and printing a triangle and parallelogram
# with the height of that number.

size = int(input("Insert size: "))
for i in range(1, size + 1):
    separator = "%" + str(size - i) + "s%s%" + str((size - i) * 2) + "s%s"
    print(separator % ("", "*" * (i*2 - 1), "", "*" * size))
