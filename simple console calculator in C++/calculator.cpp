#include <iostream> //import the standard lib
#include <cctype> //import cctype lib
using namespace std; // use std namespace

//function that resolves the calcule and show the result
void calculate(float first, float second, char op){ //receive the numbers and the operation
    //initialize the result variable
    float result;

    //check the operation and insert the calc in result
    if(op == '+'){//if is a sum
        result = first + second;
    } else if(op == '-'){ //if is a sub
        result = first - second;
    } else if(op == '*'){ //if is a multi
        result = first * second;
    }else if(op == '/'){ //if is a div 
        result = first / second;
    } else{ //if isn't any of other, is a percent calc
        result = second * (first / 100);
    }

    //show the calc and the result
    cout << first << " " << op  << " " << second << " = " << result;

    //skip a line
    cout << endl;
}

//funcion that checks if the user will use the calculator again
bool stopOrNo(){
    //initialize the variable that will check
    char checkStop = ' ';

    //while the checkStop is 'y' or 'n'
    while(checkStop == ' '){
        //ask to the user if the calculator will be used again
        cout << "Do you want to stop the calculator? [type 'y' ou 'n']";
        cin >> checkStop; //capture the result

        //check if the char inserted is correct
        if(tolower(checkStop) != 'y' && tolower(checkStop) != 'n'){ //if isn't
            checkStop = ' ';  //checkStop will return to the first value
            cout << "\nINSERT 'y' OR 'n'\n\n"; //show that is an error
        }
    }

    //if the calculator will not stop
    if(checkStop == 'n'){
        return true; //return true
    } else { //if will
        return false; //return false
    }
}

//main function 
int main(){
    //array with the operations and the names
    string operations[5][2] = {
        {"+", "sum"},
        {"-", "sub"},
        {"*", "mult"},
        {"/", "divide"},
        {"%", "percent"}
    };
    //char that will receive the operation
    char operationSelected = ' ';
    //variables of the numbers that the user will insert
    float numberOne, numberTwo;
    //boolean variable that checks if the calculator will be used again
    bool stillCalc = true;

    //start the calculator
    cout << "Welcome to the C++ calculator!\n";
    //while the check = true
    while(stillCalc == true){
        //request the first number
        cout << "insert the first number: ";
        //insert in numberOne
        cin >> numberOne;
        //skip line
        cout << endl;

        //while any operation is selected
        while(operationSelected == ' '){
            cout << "Insert the operation you want:\n";

            //for that show the options of operation
            for(int i = 0; i < 5; i++){
                cout<< "type " << operations[i][0] << " to " << operations[i][1] << endl;
            }

            //request the operation
            cout << "type your operation: ";
            //capture the operation
            cin >> operationSelected;

            //check if the operations is valid
            if(operationSelected != '+' && operationSelected != '-' && operationSelected != '*' && operationSelected != '/' && operationSelected != '%'){ //if isn't
                //reset operationSelected
                operationSelected = ' ';
                //show the error
                cout << "\nInsert one of the options!\n";
            }
        }

        //request the second number
        cout << "insert the second number: ";
        //insert in numberTwo
        cin >> numberTwo;
        //skip line
        cout << endl;

        //start the function calculate, passing the numbers and the operation
        calculate(numberOne, numberTwo, operationSelected);

        //capture if the user will calculate again
        stillCalc = stopOrNo();
    }
    //if the calculator will be stoped, show this message
    cout << "Thanks for calculate\n";

    return 0;
}