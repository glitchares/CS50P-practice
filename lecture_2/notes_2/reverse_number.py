# input of a positive number
#print that number reverse
#100 case
def main():
    print(reverse_number(get_number()))

def get_number():
    while True:
        n = int(input("Insert a positive number: "))
        if n > 0:
            return n

def reverse_number(n):
    reversed_number = 0
    while n != 0:
        last_digit = n % 10
        reversed_number = (reversed_number * 10) + last_digit
        n = n // 10 
    return reversed_number 


main()