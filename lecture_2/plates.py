import string 

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if no_punctuation(s) and startswith_2_letters(s) and correct_length(s) and numbers_at_end(s):
        return True
    else:
        return False
    
def no_punctuation(s):
    if not any(char in string.punctuation for char in s):
        return True
    else:
         return False

def correct_length(s):
    if 1 < len(s) < 7:
        return True
    else:
        return False

def startswith_2_letters(s):
    s = s[0:2]
    if s.isalpha():
        return True 
    else:
        return False
    
#def no_numbers(s):
 #   return not any(char.isdigit() for char in s)

def numbers_at_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            first_digit = i
        return s.index(first_digit)
          
    if s[first_digit:].isnumeric():
            return True 
    else:
       return False

main()

        
    
