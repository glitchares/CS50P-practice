# input positive number.
# add individual digits.

def main():
    print(sum_digits(get_number()))

def get_number():
    while True:
        n = int(input("Insert a positive number: "))
        if n > 0:
            return n 


def sum_digits(n):
    digits = 0
    while n != 0:
        last_digit = n % 10
        digits += last_digit
        n = n // 10
    return digits
        


main()