#Calculator



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Invalid input"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

again = "yes"

num1 = int(input("What's the first number?: "))



while again not in ["n", "no", "nope"]:
    num2 = int(input("What's the second number?: "))
    for operation in operations:
        print(operation + "\n")

    operation_choice = input("Choose operation what you need:\n")
    result = operations[operation_choice](num1, num2)
    print(f"{num1} {operation_choice} {num2} = {result}")
    if result == "Invalid input":
        print("You can't proceed with this calculation...")
        start_again = input("Do you want to start from the beginning?(y/n)").lower()
        if start_again in ["y", "ye", "yes"]:
            again = "yes"
            num1 = int(input("What's the first number?: "))
            continue
        again = "no"
        continue
    num1 = result
    again = input(f"Do you want to continue calculating with {result} (y/n)").lower()

print("Goodbye!\n")

