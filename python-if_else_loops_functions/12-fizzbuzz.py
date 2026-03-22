#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            res = "FizzBuzz"
        elif i % 3 == 0:
            res = "Fizz"
        elif i % 5 == 0:
            res = "Buzz"
        else:
            res = i

        if i == 100:
            print("{}".format(res), end="")
        else:
            print("{}".format(res), end=" ")
    print("")
