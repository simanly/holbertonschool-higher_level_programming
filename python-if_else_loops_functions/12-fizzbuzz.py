#!/usr/bin/python3

def fizzbuzz_logic(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number

def fizzbuzz():
    for number in range(1, 101):
        result = fizzbuzz_logic(number)�ен
        if number < 100:
            print("{}".format(result), end=" ")
        else:
            print("{}".format(result))
