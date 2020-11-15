# Ex 03 - Calculating the sum of all the odd numbers
# under 400,000 in the Fibonacci sequence.

# declaring the first two elements in the sequence in a variables.
previous_element = 1
next_element = 1
# declaring a variable of the sum of all the odd numbers under 400,000
# declaring him as "previous_element"(=1) because we want to calculate also the first element
# in the sequence.
sun_of_odd_numbers = previous_element
# running in a loop until the next index in the Fibonacci sequence is over to 400,000.
while next_element <= 400000:
    # declaring a temp variable in order not to lose "next_element"'s value later on,
    # for assigning the "previous_element" to be equal to it.
    tmp_next_element = next_element
    # calculating the next element in the sequence
    next_element = next_element + previous_element
    # assigning the previous_element to be equal to the next element in the sequence
    previous_element = tmp_next_element
    # checking if the "previous_element" is an odd number, and if so, adding him to the sum.
    # checking with "previous_element" and not with the "next_element" because the last calculation
    # of the next element in the sequence is over 400,000.
    if previous_element % 2 != 0:
        sun_of_odd_numbers += previous_element

# printing the sum of all the odd numbers in the Fibonacci sequence under 400,000.
print("The sum of all odd numbers in Fibonacci sequence is:", sun_of_odd_numbers)
