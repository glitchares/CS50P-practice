
#Purpose: print each name alongside its position,
#but formatted like a numbered list starting from 1 

def main():
    roster = ["Mariah", "Mathew", "Miracle", "Marchello", "Oliviah"]

    for i in range(len(roster)):
        print(f"{i+1}. {roster[i]}")

    print(f" Last item: {roster[-1]}")

main()