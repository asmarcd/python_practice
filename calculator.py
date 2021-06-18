num1 = float(input("Enter a number: "))
operator = input("Choose an operation +, -, *, or /: ")
num2 = float(input("Enter another number: "))

def calculate(first, op, second):
    if op == "+":
        return first+second
    elif op == "-":
        return first-second
    elif op=="*":
        return first*second
    elif op=='/':
        return first/second
    else: return "incorrect operator"

print(calculate(num1, operator, num2))
 