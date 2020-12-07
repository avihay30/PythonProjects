# Question 1 - getting an number of players and generating
# to each player 10 numbers(in range of 1 - 100), and printing the 
# winner(the first player that makes the longest ascending arithmetic sequence).

# importing random for generate_list() function.
import random


def longestSubarray(a, n):
    """ Function longestSubarray gets a list of numbers
        and the size of that list.
        and returns the size of longest ascending arithmetic sequence 
        in that list.
    """
    # declaring "counters_list" that will contains all the sizes of the
    # ascending arithmetic sequence in the "a".
    counters_list = []
    # declaring "counter" with the value 1, that represent the size of
    # ascending arithmetic sequence while running the loop.
    counter = 1
    # running in a loop until before last element in the list
    # (because we are checking if the element[i] is smaller than the next element).
    for i in range(n - 1):
        # checking if the pair of elements(element[i], element[i+1])
        # are making an ascending arithmetic sequence.
        if a[i] < a[i + 1]:
            # if so, incrementing the counter by 1.
            counter += 1
        # if the pair are not in ascending order, or equal.
        else:
            # adding the last counter to the "counters_list".
            counters_list.append(counter)
            # resetting the counter to 1 again.
            counter = 1
    # adding the last counter in the loop to the "counters_list".
    counters_list.append(counter)
    # returning the maximum value in the "counters_list"
    return max(counters_list)


def generate_list(ticket_size):
    """ Function generate_list gets a ticket_size,
        and returns a list with length of ticket_size 
        with randomized integer numbers between [1, 99].
    """
    # declaring an empty list variable
    list = []
    # running in a loop "ticket_size" times.
    for i in range(ticket_size):
        # every iteration appending new random number to the list.
        list.append(random.randint(1, 99))
    # returning the fully randomized list with length of "ticket_size".
    return list


def print_ticketArray(a, n):
    """ Function print_ticketArray gets a list,
        and prints all the elements of the list in the same line
    """
    # running a loop of all the elements of the list.
    for i in range(n):
        # in each iteration printing each element with space afterwards.
        print(a[i], end=" ")


def play(number_of_players):
    """ Function play is the main function of the program, 
        it gets the "number_of_players" from the user and summons the 
        right functions in order to declare the winner
        (the first player that makes the longest ascending arithmetic sequence) 
        of the lottery game.
    """

    # declaring an empty list that will contains 
    # all the generated list of each player.
    all_players_list = []
    # declaring an empty list that will contains the sizes of
    # longest ascending arithmetic sequence of 
    # each player(according to player index).
    list_of_longest_subarray = []
    # declaring an constant value for readability.
    list_size = 10
    # running in a loop "number_of_players" times.
    for i in range(number_of_players):
        # generating a list for each player an appending it 
        # to the "all_players_list".
        all_players_list.append(generate_list(list_size))
        # printing the introduction of the 
        # ticket list(i + 1 for not calling first player -> 0).
        print("player", i + 1, "ticket: ", end="")
        # printing the ticket list.
        print_ticketArray(all_players_list[i], list_size)
        # printing an empty line for separating a player from next player.
        print()
        # in each iterating calling the function "longest_subarray" 
        # for each player and appending the returned 
        # value the "list_of_longest_subarray".
        list_of_longest_subarray.append(
            longestSubarray(all_players_list[i], list_size))

    # declaring a "winner_number" for readability in the next print.
    # the variable gets the first index that equal to maximum value 
    # in the "list_of_longest_subarray",
    # and that index represent the index of the winner, we added 1 to 
    # the index because the count of the players starts 
    # with number 1(not 0 like in a list).
    winner_number = \
        list_of_longest_subarray.index(max(list_of_longest_subarray)) + 1
    # printing the winner.
    print("***Player number", winner_number, "is the winner***")


# getting a number of players from the user.
num_of_players = \
    int(input("Please enter the number of players in the lottery game: "))
# running the function "play" with the "num_of_players".
play(num_of_players)
