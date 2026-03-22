#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            res = "FizzBuzz"
        elif number % 3 == 0:
            res = "Fizz"
        elif number % 5 == 0:
            res = "Buzz"
        else:
            res = number

        if number < 100:
            print("{}".format(res), end=" ")
        else:
            print("{}".format(res))
