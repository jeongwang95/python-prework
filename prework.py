# Coding Temple Python Prework
# Jeong Wang

# Q1
# input user_name as a string and the function prints "hello_user_name!"
def hello_name(user_name):
    print("hello_" + user_name + "!")

# testing
# hello_name("jeongwang")

# Q2
# prints all of the odd number from 1 to 100
def first_odds():
    for number in range(1,101):
        if number%2 == 1:
            print(number)

# testing
# first_odds()

# Q3
# input a numbered list then it returns the maximum number in the list
def max_num_in_list(a_list):
    return max(a_list)

# testing
# print(max_num_in_list([1,100,101,99,50,8]))

# Q4
# input a year and function will return true if it is a leap year
# and return false if it is not a leap year
def is_leap_year(a_year):
    if a_year%4 == 0 and a_year%100 == 0 and a_year%400 == 0:
        return True
    elif a_year%4 == 0 and a_year%100 != 0:
        return True
    else:
        return False

# testing
# print(is_leap_year(2000))
# print(is_leap_year(2004))
# print(is_leap_year(2010))      
# print(is_leap_year(2100))
# print(is_leap_year(2400)) 

#Q5
# input a list of number and returns true if the numbers in the list
# are in consecutive order
def is_consecutive(a_list):
    # store the first number in the list
    previous_num = a_list[0]
    # copy of a_list excluding the first number in a_list
    new_list = a_list[1:]

    for number in new_list:
        # check if the current number is the consecutive 
        # number from the previous number
        if number-previous_num != 1:
            return False
        # if current number is consecutive, current 
        # number now becomes the previous number
        else:
            previous_num = number
    
    return True

# testing
# print(is_consecutive([1,2,3,4,5]))
# print(is_consecutive([1,2,4,5]))
# print(is_consecutive([4,5,6,7]))
# print(is_consecutive([5,4,3]))