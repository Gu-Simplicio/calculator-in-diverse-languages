#include <iostream>
#include <cctype>
using namespace std;

void calculate(float first, float second, char op){
    float result;

    if(op == '+'){
        result = first + second;
        cout << first << " + " << second << " = " << result;
    } else if(op == '-'){
        result = first - second;
        cout << first << " - " << second << " = " << result;
    } else if(op == '*'){
        result = first * second;
        cout << first << " * " << second << " = " << result;
    }else if(op == '/'){
        result = first / second;
        cout << first << " / " << second << " = " << result;
    } else{
        result = second * (first / 100);
        cout << first << "%" << second << " = " << result;
    }
    cout << endl;
}

bool stopOrNo(){
    char checkStop = ' ';

    while(checkStop == ' '){
        cout << "Do you want to stop the calculator? [type 'y' ou 'n']";
        cin >> checkStop;

        if(tolower(checkStop) != 'y' && tolower(checkStop) != 'n'){
            checkStop = ' ';
            cout << "\nINSERT 'y' OR 'n'\n\n";
        }
    }

    if(checkStop == 's'){
        return true;
    }   
}

int main(){
    string operations[5][2] = {
        {"+", "sum"},
        {"-", "sub"},
        {"*", "mult"},
        {"/", "divide"},
        {"%", "percent"}
    };
    char operationSelected = ' ';
    float numberOne, numberTwo;

    cout << "Welcome to the C++ calculator!\n";
    while(true){
        cout << "insert the first number: ";
        cin >> numberOne;
        cout << endl;

        while(operationSelected == ' '){
            cout << "Insert the operation you want:\n";

            for(int i = 0; i < 5; i++){
                cout<< "type " << operations[i][0] << " to " << operations[i][1] << endl;
            }

            cout << "type your operation: ";
            cin >> operationSelected;

            if(operationSelected != '+' && operationSelected != '-' && operationSelected != '*' && operationSelected != '/' && operationSelected != '%'){
                operationSelected = ' ';
                cout << "\nInsert one of the options!\n";
            }
        }

        cout << "insert the first number: ";
        cin >> numberTwo;
        cout << endl;

        calculate(numberOne, numberTwo, operationSelected);

        if(stopOrNo()){
            break;
        }
    }
    cout << "Thanks for calculate\n";

    return 0;
}