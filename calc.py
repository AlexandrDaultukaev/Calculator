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

def validator(num1, num2):
    if num1.isalpha() or num2.isalpha():
        print("Your numbers have symbol(s) other than digits!\n")
        exit()
    if num1 in [" " * len(num1)] or num2 in [" " * len(num2)]:
        print("There must be no spaces in your input!")
        exit()
 

def calculator():
    again = "yes"
    num1 = input("What's the first number?: ")
    while again not in ["n", "no", "nope"]:
        num2 = input("What's the second number?: ")
        validator(num1, num2)
        num1 = int(num1)
        num2 = int(num2)
        for operation in operations:
            print(operation + "\n")
        operation_choice = input("Choose operation what you need:\n")
        result = operations[operation_choice](num1, num2)
        print(f"{num1} {operation_choice} {num2} = {result}")
        if result == "Invalid input":
            print("You can't proceed with this calculation...")
            return
        num1 = result
        again = input(f"Do you want to continue calculating with {result} (y/n): ").lower()

start_over = "yes"
while start_over in ["y", "yes", "ye"]:
    calculator()
    start_over = input("Do you want to start from beginning?(y/n): ")

print("Goodbye!\n")

