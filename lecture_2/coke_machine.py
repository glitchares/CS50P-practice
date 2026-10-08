def main():
    print(check_amount_due(verify_new_coin()))

def verify_new_coin():
    while True:
        coin_inserted = int(input("Insert coin: "))
        match coin_inserted:
            case 25 | 10 | 5:
                return coin_inserted

def check_amount_due(coin_inserted):
    total = 0
    while total < 50:
        total += coin_inserted
        if total < 50:
            amount_due = 50 - total 
            print(f"Amount Due: {amount_due}")
            coin_inserted = verify_new_coin()
    change_owed = total - 50
    return f"Change owed: {change_owed}"
main()

