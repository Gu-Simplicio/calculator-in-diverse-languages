#function that check if the calculator will stop
def check_stop():
    #variable that will receive the answer
    answer = ''
 
    #while the answer isn't true and isn't false
    while answer != True and answer != False:
        #capture the answer
        char_insert = input("Do you want to stop the calculator, y or n?").lower()
        
        #check if is true or false
        if(char_insert == 'y'):
            answer = True
        elif(char_insert == 'n'):
            answer = False
        else: #if isn't y or n
            print("INSERT 'y' OR 'n'!")

    return answer #return the answer

#function that will make the calc and show the result
def calculate(first, second, op):
    if(op == '+'):
        result = f"{first} + {second} = {first + second}"
    elif(op == "-"):
        result = f"{first} - {second} = {first - second}"
    elif(op == "*"):
        result = f"{first} X {second} = {first * second}"
    elif(op == "/"):
        result = f"{first} / {second} = {first / second}"
    else:
        result = f"{first}%{second} = {second * (first / 100)}"

    print(result)
    
def show():
    while True:        
        first_number = float(input("Insert the first number: "))
        second_number = float(input("Insert the second number: "))

        operation = ''

        while operation == '':
            print("\nChoose which operation you want to do")
            print("insert + to sum")
            print("insert - to submit")
            print("insert * to multiplie")
            print("insert / to divide")
            print("insert %  to get the percent")

            operation = input("insert the operation: ")

            if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '%'):
                operation = ''
                print("\nINSERT ONE OF THE OPTIONS")

        calculate(first_number, second_number, operation)

        stop_or_no = check_stop()
        if(stop_or_no):
            print("Thanks for calculate!")
            break

print("WELCOME TO THE SIMPLE PYTHON CALCULATOR!")
show()