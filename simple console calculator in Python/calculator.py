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
    #check which calcule was inserted and show the result
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
    
#function that will start the calculator
def calculator():
    #while true..
    while True:  
        #capture the numbers      
        first_number = float(input("Insert the first number: "))
        second_number = float(input("Insert the second number: "))

        operation = '' #start the operation variable

        #while the operation isn't defined
        while operation == '':
            #preint the options
            print("\nChoose which operation you want to do")
            print("insert + to sum")
            print("insert - to submit")
            print("insert * to multiplie")
            print("insert / to divide")
            print("insert %  to get the percent")

            #capture the operation
            operation = input("insert the operation: ")

            #if the operation isn't valid
            if(operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '%'):
                operation = '' #reset operation
                print("\nINSERT ONE OF THE OPTIONS") #show the error

        #start the function calculate
        calculate(first_number, second_number, operation)

        if(check_stop()): #check if the user will calculate again
            #if the calculator will stop, show the message
            print("Thanks for calculate!")
            break #break the function

#start the calculator
print("WELCOME TO THE SIMPLE PYTHON CALCULATOR!")
calculator()