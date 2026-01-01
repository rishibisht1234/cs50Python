


def interpret(expression):
    e=expression.strip()
    e=e.split(" ")
    x=float(e[0])
    y=e[1]
    z=float(e[2])

    match y:
        case "+":
            return x+z
        case "-":
            return x-z
        case "*":
            return x*z
        case "/":
            if z==0:
                return "z cannot be 0"
            else:
                return x/z
        case _:
                return "expression is not correct"




def main():
    expression=input("Expression : ")
    result=interpret(expression)
    if isinstance(result, float):
        print(f"{result:.1f}")
    else:
        print(result)

main()
