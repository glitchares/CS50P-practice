def main():
    message = input("Input: ")
    omitting_vowels(message)  

def omitting_vowels(message):
    vowels = ["a", "e", "i", "o", "u"]
    new_str = ""
    for c in message:
        if not c.lower() in vowels:
            new_str += c
    print(f"Output: {new_str}")  

main()


