#positive_sum
#input = numbers greater than 0, int
#print the sum of all integers 1 to n

def main():
    total = sum_up(get_number())
    print(total)
    

def get_number():
    while True:
        n = int(input("Insert a natural number: "))
        if n > 0:
            return n

def sum_up(n):
    total = 0
    for number in range(n):
        total = total + (number + 1)
    return total
        


main()
