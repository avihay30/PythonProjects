# 1-
# getting the information of the user's weight and height
weight = int(input("Enter weight (in kg): "))
height = int(input("Enter height (in cm): "))

# calculate his BMI (BMI = weight (kg) / (height (m))^2)
bmi = weight / (height / 100) ** 2

# printing the weight status according to the bmi calculation
if bmi < 18.5:
    print("Underweight.")
elif bmi < 25:
    print("Normal weight.")
elif bmi < 30:
    print("Increased weight.")
elif bmi < 40:
    print("Obese.")
elif bmi >= 40:
    print("Very high obese.")

# 2-
# getting the 4-digits number from the user
number = int(input("Enter a positive 4-digits number: "))

# checking if the number is negative
if number < 0:
    print(number, "is a negative number, Bye bye.")
# checking if the number is 3-digits number
elif number < 1000:
    print(number, "is not a 4-digits number, Bye bye.")
# checking if the number is 5-digits number
elif number > 9999:
    print(number, "is not a 4-digits number, Bye bye.")
# continuing with the fact that number is a 4-digits number
else:
    # separating the digits to different variables
    thousands = number // 1000
    hundreds = number // 100 % 10
    tens = number // 10 % 10
    units = number % 10
    # checking if all digits are the same
    if thousands == hundreds == tens == units:
        print("all digits are the same.")
    else:
        # calculating the difference between each 2 digits in the number
        difference1 = thousands - hundreds
        difference2 = hundreds - tens
        difference3 = tens - units
        # checking if the digits making an arithmetic sequence
        if difference1 == difference2 == difference3:
            # checking if the arithmetic sequence is increasing
            if difference1 < 0:
                print("Increasing arithmetic sequence (from left to right).")
            # checking if the arithmetic sequence is decreasing
            else:
                print("Decreasing arithmetic sequence (from left to right).")
        # checking if the digits making an increasing sequence
        elif thousands <= hundreds <= tens <= units:
            print("Ascending sequence (from left to right).")
        # checking if the digits making an descending sequence
        elif thousands >= hundreds >= tens >= units:
            print("Descending sequence (from left to right).")
        # checking if the digits are not descending or increasing sequence
        else:
            print("Non decreasing and non increasing.")

# 3-
# getting the number of children of the user
children = int(input("Enter number of children: "))
# getting the monthly salary of the user
salary = int(input("Enter your monthly salary: "))
# asking the user if he has done military or civilian service
has_done_service = input("Military/Civilian service? \n"
                         " For YES enter 'y', otherwise any other character: ")
# printing empty space for readability
print()
# casting has_done_service(string) variable to an boolean type for readability
has_done_service = True if has_done_service == 'y' else False
# checking if condition 3 is met
if salary > 7500:
    # printing mortgage is approved and the calculation of 30% of the salary
    print("The mortgage is approved at amount of:", int(salary * 0.3))
# checking if condition 1 or condition 2 are met
elif (has_done_service and salary >= 5000) or (children >= 4 and salary >= 4000):
    # printing mortgage is approved and the calculation of 20% of the salary
    print("The mortgage is approved at amount of:", int(salary * 0.2))
# if no condition is met
else:
    # printing mortgage isn't approved
    print("The mortgage is not approved.")
    
    
############ --- just practice   
str_digit = input("Enter digit (0-9, -1 for exit): ")
number = ""
while str_digit != "-1":
    number += str_digit
    str_digit = input("Enter digit (0-9, -1 for exit): ")
    
print("this is number: ", number)
reversed_number = ''
for char_digit in str(number):
    reversed_number = char_digit + reversed_number
print("this is reversed number =", reversed_number)


a1,d,n = eval(input("Enter a1, d and n in arithmetic sequence: "))

for i in range(a1, n+1, d):
    print(i)
