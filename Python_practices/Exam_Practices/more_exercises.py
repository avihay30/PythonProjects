# some exercise from
# "https://rt-ed.co.il/articles/python-language-questions-and-answers/" website
import random


def question_1():
    sum = 0
    counter = 0
    while True:
        input_value = input("Enter a number: ")
        if input_value == "q":
            break
        sum += int(input_value)
        counter += 1
        continue
    return sum / counter


def question_2(integers_list, number):
    new_list = []
    for i in range(len(integers_list)):
        if integers_list[i] % number != 0:
            new_list.append(integers_list[i])
    integers_list.clear()
    integers_list.extend(new_list)
    return integers_list


def question_3(string):
    """ is palindrome """
    if len(string) <= 1:
        return True
    if len(string) >= 2 and string[0] == string[-1]:
        return question_3(string[1:-1])
    return False


def question_4():
    user_guess = eval(input("Enter 3 numbers [0-9], (add comma as a separator): "))
    computer_roll = []
    for i in range(len(user_guess)):
        computer_roll.append(random.randint(0, 9))

    for i in range(len(user_guess)):
        if user_guess[i] not in computer_roll:
            print("You Lose")
            break
    else:
        print("You Win")


def question_6(digits_list):
    counters_list = [0] * 10
    for i in range(len(digits_list)):
        counters_list[digits_list[i]] += 1
    return counters_list


def main():
    # print(question_1())
    # print(question_2([2, 3, 4, 5, 6], 2))  # [3, 5]
    # print(question_3("racecar"))  # = True
    # question_4()
    # print(question_6([2, 2, 2, 2, 2, 2, 6, 6, 0, 0]))  # = [2, 0, 6, 0, 0, 0, 2, 0, 0, 0]
    return


main()
