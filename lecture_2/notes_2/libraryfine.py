def main():
    calculate_fine(get_book_days())
    
def get_book_days ():
    while True: 
        days_overdue = int(input("How many days is this book overdue?: "))
        if days_overdue > -1:
            return days_overdue
        
def calculate_fine(days_overdue):
    book_overdue_fine = 10
    total_fine = 0

    while days_overdue > 0:
        total_fine += book_overdue_fine * days_overdue
        print(f"Running total fine: {total_fine}")
        days_overdue = get_book_days()

    print(f"Final total fine: {total_fine}")
    

main()