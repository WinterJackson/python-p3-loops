#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countdown = 10
    while countdown >= 1:
        print (countdown)
        countdown -=1
    print ("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list

input_list = [10, 12, 23, 4, 15]
result = square_integers(input_list)
print(result)

def fizzbuzz():
    # code goes here!
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

fizzbuzz()


# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# player_heights = [height * 7920 for height in player_heights]

# print (player_heights)