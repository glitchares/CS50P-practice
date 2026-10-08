#input: a positve number
#a cardinal
def main():
    n, limit = get_data()
    calculate_multiples(n, limit)
    
def get_data():
    while True:
        n = int(input("Insert a positive number: "))
        limit = int(input("Insert amount of multiples: "))
        if n > 0 and limit > 0: 
            return n, limit
            
    

def calculate_multiples(n, limit):
    for times in range(limit):
        times += 1
        multiples = times * n
        print(multiples)

main()