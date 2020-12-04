# 1-
# getting number from the user.
number = int(input("Enter integer number: "))
# declaring a boolean variable that represent if "number" is negative.
is_negative = False

# printing the first line of the list of divisors.
print("List of divisors of", number, ":", end=" ")

# checking if number is negative.
if number < 0:
    # changing the variable "is_negative" to be true.
    is_negative = True
    # saving "number" with the absolute value of "number".
    number = abs(number)

# declaring a count variable that represent the number of natural dividers.
count = 0
# running the loop number times
for i in range(1, number):
    # checking if "i" is a natural divider of "number"
    if (number % i) == 0:
        # printing the natural divider
        # in the same line of the print above the "for".
        print(i, end=" ")
        # incrementing the counter of the dividers
        count += 1

# checking if number was negative before he was changed to his absolute value.
# adding the absolute value of number to the list,
# if he was negative in the beginning.
if is_negative:
    # printing the absolute value of the number to the list.
    print(number)
    # incrementing the counter of the dividers.
    count += 1

# checking if number is 0.
if number == 0:
    # changing count to hold the string "infinity" for the next print.
    count = "infinity"

# printing number of divisors of the "number".
print("\nnumber of divisors is:", count)

# 2-
# getting the first element in the series.
element_in_series = int(input(
    "Enter first element of Geometric Progression Series: "))
# getting the common ratio of the series.
ratio = float(input("Enter the common ratio: "))
# getting an "n" place in the series.
n = int(input("Enter Integer: "))

# printing the first line of the output.
print("Geometric Progression Series:", end=" ")
# running in a loop "n" times
for i in range(n):
    # printing the first element of the series in every iteration.
    print("%.3f" % element_in_series, end=" ")
    # multiplying and saving the new element
    element_in_series *= ratio

# 3-
# running the loop until we call "break" if char = q or Q.
while True:
    # getting the char input.
    char = input("Enter char:\
          \na or A --> average\
          \n*	   --> multiply\
          \nm	   --> minimum\
          \nM	   --> maximum\
          \n^	   --> power\
          \nQ or q --> quit\n\n")
    # checking if to stop the program.
    if char == "q" or char == "Q":
        print("Finish")
        break

    # if the user inserted not valid char, running the loop again.
    elif (not (char == "A" or char == "a" or char == "m"
               or char == "M" or char == "^" or char == "*")):
        print("Error, please try again.")
        continue

    # getting two numbers from the user.
    number1, number2 = eval(input("Enter 2 integers(like --> a, b): "))
    # I can add "continue" in each block of if, but it's redundant.
    if char == "a" or char == "A":
        # calculating the average.
        average = (number1 + number2) / 2
        # checking if the average is an integer number.
        if average % 1 == 0:
            print("The average is an integer number:", average)
        # if average isn't integer.
        else:
            print("The average is not integer number: %.3f" % average)
        # after both cases running the loop again.
    elif char == "*":
        # printing the multiplication of both numbers.
        print("The multiplication of", 
              number1, "*", number2, "is:", number1 * number2)
    elif char == "m":
        # printing the minimum of both numbers.
        print("The minimum is:", number1 if number1 < number2 else number2)
    elif char == "M":
        # printing the maximum of both numbers.
        print("The maximum is:", number1 if number1 > number2 else number2)
    elif char == "^":
        # checking if the user entered 
        # non valid operation(0 with the power of 0).
        if number1 == 0 and number2 == 0:
            print("Sorry, you can't do power of 0 on base 0")
        else:
            # printing the power of "number1" by "number2"
            power = number1 ** number2
            # checking if the power is an integer number.
            if power % 1 == 0:
                print("The power is integer number:", power)
            else:
                print("The power is not integer number: %.3f" % power)


# practice No.5
def getElementInFibonacci(number):
    previous_element = 0
    next_element = 1
    if number > 2:
        previous_element = 1
    for i in range(number - 2):
        tmp_next_element = next_element
        next_element = next_element + previous_element
        previous_element = tmp_next_element
    return next_element if number > 1 else number


def getListOfElementsInFibonacci(number):
    for i in range(number + 1):
        print(getElementInFibonacci(i), end=" ")


n = int(input("Enter number: "))
print("The number in place", n, "in Fibonacci is:", getElementInFibonacci(n))
getListOfElementsInFibonacci(n)
