# Ex 01 - Calculating the intersection coordinates of two straight lines in plane
# according to two points on each line.

# getting user inputs about the coordinates of the straight lines in plane.
lineA_x0, lineA_y0, lineA_x1, lineA_y1 = eval(input("Insert line A data: "))
lineB_x0, lineB_y0, lineB_x1, lineB_y1 = eval(input("Insert line B data: "))

# calculating the slope of a straight line.
lineA_slope = (lineA_y0 - lineA_y1) / (lineA_x0 - lineA_x1)
lineB_slope = (lineB_y0 - lineB_y1) / (lineB_x0 - lineB_x1)

# checking if the lines are parallel lines.
if lineA_slope == lineB_slope:
    print("The is no intersection between the two lines.\n"
          "try inserting different coordinates, goodbye!")
else:
    # calculating the n(unknown) for the equation "y = mx + n".
    lineA_n = lineA_y0 - lineA_slope * lineA_x0
    lineB_n = lineB_y0 - lineB_slope * lineB_x0

    # calculating the x coordinate of the intersection according to the
    # equation x = (Bn - An) / (slopeA - slopeB).
    intersection_x = (lineB_n - lineA_n) / (lineA_slope - lineB_slope)
    # calculating the y coordinate of the intersection according to the equation "y = mx + n."
    intersection_y = lineA_slope * intersection_x + lineA_n

    # printing the coordinates of the intersection.
    print("the coordinates of the intersection are: (%.2f, %.2f)" % (intersection_x, intersection_y))
