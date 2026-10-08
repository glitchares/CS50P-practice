# user's input  number greater than 0
# print factorial of n excluding 0
 
def main():
    print(factorial(get_number()))

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            return n

def factorial(n):
    total = 1
    for number in range(n):
        total = total * (number + 1)

    return total

main()