# Ex 03 - Calculating the sum of all the odd numbers
# under 400,000 in the Fibonacci sequence.

# saving the first two elements in the sequence in a variables.
previous_element = 1
next_element = 1
# creating a variable of the sum of all the odd numbers under 400,000
# saving him as previous_element(=1) because I want to calculate also the first element
# in the sequence.
sun_of_odd_numbers = previous_element
# running in a loop until the next index in the Fibonacci sequence is over to 400,000.
while next_element <= 400000:
    # saving the next_element in a temp variable in order to not lose it's value
    # later on for assigning the previous_element to be equal to it
    tmp_next_element = next_element
    # calculate the next element in the sequence
    next_element = next_element + previous_element
    # assigning the previous_element to be equal to the next element in the sequence
    previous_element = tmp_next_element
    # checking if the previous_element is an odd number and if so adding him to the sum
    # checking with previous_element and not with the next_element because there is a chance
    # that the next_element is over 400,000.
    if previous_element % 2 != 0:
        sun_of_odd_numbers += previous_element

print("The sum of all odd numbers in Fibonacci sequence is:", sun_of_odd_numbers)
