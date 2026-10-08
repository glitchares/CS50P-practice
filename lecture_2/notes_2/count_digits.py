def main():
    print(count_digits(get_number()))

def get_number():
    while True:
        n = int(input("Insert a positive number: "))
        if n > 0:
            return n


def count_digits(n):

    digits = 0

    while n != 0:
        n = n // 10 
        digits += 1

    return digits
  
    
main()
    