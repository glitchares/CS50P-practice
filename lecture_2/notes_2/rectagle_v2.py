def main():
    width, height  = get_size()
    print_rectangle(width, height)

def get_size():
    while True:
        width = int(input("Insert a valid width for the rectangle: "))
        height = int(input("Insert a valid height for the rectangle: "))
        if width > 0 and height > 0:
            return width, height
         
#Print a solid rectangle 

def print_rectangle(width, height):
    for i in range(height):
        print_row(width)

def print_row(width):
        print("#" * width)

main()