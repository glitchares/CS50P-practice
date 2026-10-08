#Math Interpreter
def main():
    expression = input("Insert an arithmethic expression: ")
    x, y, z = expression.split(" ")
    print(f"{result(x, y, z):.1f}")

def result(x, y, z): 

    x = float(x)
    z = float(z)
    
    if y == "+":
        return x + z
    
    elif y == "-":
        return x - z
    
    elif y == "/":
        return x / z
    
    elif y == "*":
        return x * z

    
main()