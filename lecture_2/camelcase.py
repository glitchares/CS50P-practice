#first letter lowercase, the each word uppercase
#convert camelcase input into snake_case

def main():
    variable = input("Insert a variable using camelCase: ")
    into_snake(variable)

def into_snake(variable):
    snaked = ""
    for character in variable:
        if character.isupper():
            character =  ("_" + character)
        snaked += character   
    print(snaked.lower())
            
main()