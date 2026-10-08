#Problem: stars.py 
#VERSION A:

def main():
    for asterik in range(5):
        print("*", end="")

    print()


main()
#VERSION B:

def main():
    for _ in range(5):
        print("*", end="")

    print()

#VERSION C:

def main():
    print ("*" * 5)

main()
 

