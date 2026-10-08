def main():
    width = get_width()
    height = get_height()
    print_rectangle(width, height)

def get_width():
    while True:
        width = int(input("Insert a valid width for the rectangle: "))
        if width > 0:
            return width
        
def get_height():
    while True:
        height = int(input("Insert a valid height for the rectangle: "))
        if height > 0:
            return height   
 
#Print a solid rectangle 

def print_rectangle(width, height):
    for _ in range(height):
        print_row(width)

def print_row(width):
        print("#" * width)

main()