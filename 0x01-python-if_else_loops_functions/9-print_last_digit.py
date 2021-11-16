#!usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastd = ((number * -1) % 10)
    else:
        lastd = number % 10
    print(lastd, end="")
    return lastd
