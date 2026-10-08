def main():
    greeting = input("Tell a greeting: ").strip().lower()
    check_greeting(greeting)

def check_greeting(greeting):
    if greeting.startswith("hello"):
        print("$0")

    elif greeting.startswith("h"):
        print("$20")

    else:
        print("$100")
main()