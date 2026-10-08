#input: a positve number
#a cardinal
def main():
    n = get_n()
    limit = get_limit()
    calculate_multiples(n, limit)
    
def get_n():
    while True:
        n = int(input("Insert a positive number: "))
        if n > 0: 
            return n

def get_limit():
    while True:
        limit = int(input("Insert amount of multiples: "))
        if limit > 0:
                return limit

def calculate_multiples(n, limit):
    for times in range(limit):
        times += 1
        multiples = times * n
        print(multiples)