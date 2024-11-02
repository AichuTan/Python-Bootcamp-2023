import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

## Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*","/"
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

#ToDO : Use the dictionary operations to perform the calculation. Multiply 4*8

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input('What is the first number?'))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        pick_operation = input('Pick an operation: ' )
        num2 = float(input('What is the next number?'))
        result = operations[pick_operation](num1,num2)
        print(f"{num1} {pick_operation} {num2} =  {result}" )
        recount = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.")
        if recount == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()