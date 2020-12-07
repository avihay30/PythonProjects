# 1-
def input_list(n):
    """ Function input_list gets an integer
        and returns a list of inputted integers with length of the integer.
    """
    original_list = []
    # running in a loop n times.
    for i in range(n):
        # every iteration appending to the empty list("original_list").
        original_list.append(int(input("%s.Enter integer: " % str(i+1))))
    
    return original_list


def create_new_list(a, x):
    """ Function create_new_list(a,x) gets an list = a, number = x,
        and returns new ordered(by x) list, all the elements 
        that are smaller the x in the beginning of the list 
        and the other afterwards(in the same order as before).
    """
    # declaring two empty list.
    b_list = []
    temp_list = []
    # running over all the elements in a list, and checking 
    # if they are smaller than x.
    for element in a:
        if element < x:
            # if smaller appending to the "b_list"
            b_list.append(element)
        else:
            # if bigger/equal appending to a temp list
            # for maintaining the original order of the list.
            temp_list.append(element)

    # adding all the elements of the temp list to the end of the the new b_list.
    for element in temp_list:
        b_list.append(element)
    
    return b_list


def main():
    """ Function main summons the right functions
        and prints in the end the original list and the modified list
    """
    # declaring a variable named "origin_list" for readability 
    # that contains the inputted list of integers.
    # calling the function with the number 7 as required in the exercise.
    origin_list = input_list(7)
    # declaring a variable named "equivalent" that contains a 
    # inputted number from the user.
    equivalent = int(input("Enter x: "))
    # printing the original list.
    print("Original list:", origin_list)
    # declaring a variable named "new_list" for readability 
    # that contains the new modified list.
    new_list = create_new_list(origin_list, equivalent)
    # printing the new list.
    print("New list:", new_list)


# running main function.
main()


# 2-
def create_list_of_lap_time(n):
    """ Function create_list_of_lap_time gets an integer
        and returns a list of inputted integers with length of the integer.
    """
    times_list = []
    # running in a loop n times.
    for i in range(n):
        # every iteration appending to the empty list("times_list").
        times_list.append(float(input("%s.Enter time: " % str(i+1))))

    return times_list


def my_avg(lap_times_list):
    """ Function my_avg gets a list of lap times, 
        and returns the average of the times
    """
    sum = 0
    # running in loop on every element in "lap_times_list".
    for element in lap_times_list:
        # adding to sum each element in the list.
        sum += element
    # calculating the average time.
    avg_time = sum / len(lap_times_list)

    return avg_time


def runners_below_avg(avg, lap_times_list):
    """ Function runners_below_avg gets an average time and a list of integers,
        and returns the amount of elements below the average.
    """
    count = 0
    # running in loop on every element in "lap_times_list".
    for element in lap_times_list:
        # checking if the element is smaller than average 
        # and if so incriminating count.
        if element < avg:
            count += 1
    
    return count


def main():
    """ Function main gets from the user the number of runners 
        and summons the right functions, in the end printing the 
        calculated average and the number of runners, running below average.
    """
    runners = int(input("Enter number of runners: "))
    # calling "create_list_of_lap_time" function and saving in a variable.
    lap_times_lst = create_list_of_lap_time(runners)
    # calling "my_avg" function and saving in a variable.
    average_time = my_avg(lap_times_lst)
    # calling "runners_below_avg" function and saving in a variable.
    num_of_fast_runners = runners_below_avg(average_time, lap_times_lst)

    # printing the results to the user.
    print("Time average is %.3f" % average_time)
    print("The number of runners, running below average time is", 
          num_of_fast_runners)


# running main function.
main()


# 3-
def get_list_amount_of_digit(n):
    """ Function get_list_amount_of_digit gets an integer, 
        and creates a counters list.
    """
    # creating a list with length of 10 and all elements are 0.
    # every index represent the number of appears of that digit.
    amount_list = [0] * 10
    # running in loop on every digit in "n".
    for digit in str(n):
        # incrementing the element in index = digit.
        amount_list[int(digit)] += 1

    return amount_list


def print_appear_times(amount_digit_list):
    """ Function print_appear_times get a list
        and prints the element(if not 0) and the index
    """
    # running in loop length of "amount_digit_list" times.
    for i in range(len(amount_digit_list)):
        # if the element is not 0.
        if amount_digit_list[i] != 0:
            # printing the element in 
            # index "i"(represents the number of appearances)
            # and "i"(represents the actual number)
            print("The digit %s appears %s times." %
                  (i, amount_digit_list[i]))


def get_frequent_digit(cnt_list, maximum_amount):
    """ Function print_appear_times gets a list and a number
        that represents the maximum element in the list,
        and returns the indexes of elements that are equal to that max number.
    """
    most_freq_digits = []
    # running in loop length of "cnt_list" times.
    for i in range(len(cnt_list)):
        # if the element in list is equal to the "maximum_amount".
        if cnt_list[i] == maximum_amount:
            # if so, appending to the empty list.
            most_freq_digits.append(i)

    return most_freq_digits


def print_most_freq(freq_dig):
    """ Function print_most_freq gets a list 
        and print all the element of that list 
    """
    print("The most frequent digit/s is/are: ", end="")
    for element in freq_dig:
        print(element, end=" ")


def main():
    """ Function main gets input from the user of a integer number
        and returns the number of appearances of each digit in that number.
    """
    number = int(input("Enter integer: "))
    # if number is negative changing it to positive.
    number = abs(number) if number < 0 else number
    # gets a counters list by the get_list_amount_of_digit function.
    counters_list = get_list_amount_of_digit(number)
    # calls the "print_appear_times" function for printing for user.
    print_appear_times(counters_list)
    # saving the maximum value in the counters_list in a variable.
    max_amount = max(counters_list)
    # get the actual digits that are the most frequent.
    freq_digits = get_frequent_digit(counters_list, max_amount)
    # calls the "print_most_freq" function for printing 
    # to user the frequent digit\s.
    print_most_freq(freq_digits)
    # printing how many times the digits appeared in the inputted number.
    print("\nIt occurs times:", max_amount)


# running main function.
main()
