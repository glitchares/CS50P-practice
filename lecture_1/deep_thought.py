#The Great Question of life
#input: 42 forty two 42. yes 
#otherwise No

def main():
    great_question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? " ).strip().lower()
    
    match great_question:
        case "42"|"forty-two"|"forty two":
            print("Yes")
        case _:
            print("No")
    

main()
