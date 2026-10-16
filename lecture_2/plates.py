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
                if s[i:].startswith("0"):
                    return False
                else:
                    return s[i:].isnumeric()
        return True
            
main()

        
 #  if s[i].isdigit() and s[i] != "0": 

'''
def numbers_at_end(s):
        for i in range(len(s)):
            if s[i].isdigit():
                if s[i] != "0":
                    return s[i:].isnumeric()
        return True
            
main()

'''

'''
def numbers_at_end(s):
        for i in range(len(s)):
            if s[i].isdigit():
                if not s[i:].startswith("0"):
                    return s[i:].isnumeric()
        return True
            
'''