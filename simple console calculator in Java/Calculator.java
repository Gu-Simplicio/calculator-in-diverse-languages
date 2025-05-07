import java.util.Scanner; //import the scanner from java

//class Calculator
public class Calculator {
    //main method
    public static void main(String[] args) {
        //char that will receive the operation  
        char operation;
        //boolean that receive if the calculator will be used again
        boolean stillCalc = true;
        //variables that will receive the numbers to calculate
        double firstNumber, secondNumber;
        //create a scanner object
        Scanner scanner = new Scanner(System.in);

        //start the calculator
        System.out.println("WELCOME TO JAVA CALCULATOR!");
        //do..while of the calculator
        do{
            //request the first number
            System.out.print("Insert the first number: ");
            //capture with scanner
            firstNumber = scanner.nextDouble();

            //request the operation with the method captureOperation(), passing the scanner
            operation = captureOperation(scanner);

            //request the second number
            System.out.print("\nInsert the second number: ");
            //capture with scanner
            secondNumber = scanner.nextDouble();

            //start the method calculate()
            calcule(firstNumber, operation, secondNumber);

            //check if the calculator will be used again with the method checkIfStillCalc(), passing the scanner
            stillCalc = checkIfStillCalc(scanner);
        }while(stillCalc == true); //check the stillCalc
        //if the calculator is stoped, show this message
        System.out.print("Thanks for calculate!");
        //close the scanner
        scanner.close();
    }

    //method that check the operation to be used
    static char captureOperation(Scanner scanner){
        //char that will receive the operation
        char opSelected = ' ';
        //array with the operations and their names
        String[][] operations = {
            {"+", "sum"},
            {"-", "sub"},
            {"*", "mult"},
            {"/", "div"},
            {"%", "percent"}
        };

        //do..while that will receive the operation
        do{
            //loop for that show the options of operation
            for (int i = 0; i < operations.length; i++) {
                System.out.printf("type %s to %s\n", operations[i][0], operations[i][1]);
            }

            //request the operation
            System.out.print("Insert your operation: ");
            //capture the operation with scanner and capturing the first letter inserted
            opSelected = scanner.next().charAt(0);

            //variable that will help the for loop
            int aux = 0;
            //loop for that will check if the operation is valid
            for(int i = 0; i < operations.length; i++){
                //if is a charactere different of the valids, increment the aux
                if(opSelected != operations[i][0].charAt(0)) aux++;
            }
            //if the aux is equal the total operations 
            if(aux == operations.length){
                //show that is an error 
                System.out.print("\nInsert a correct operation!\n\n");
                opSelected = ' '; //reset opSelected
            }
        }while(opSelected == ' ');//check if opSelected == ' '
        
        //return opSelected
        return opSelected;
    }

    //method that will check if the calculator will be used again
    static boolean checkIfStillCalc(Scanner scanner){
        //char variable that will receive the check
        char check = ' ';

        //while the check isn't y or 'n'
        while(check != 'y' && check != 'n'){
            //ask if the user will use the calculator again
            System.out.print("\nDo you want to calculate again? [type 'y' or 'n']: ");
            //capture the answer with scanner
            check = scanner.nextLine().charAt(0);

            //if the check is not 'y' or 'n'
            if(check != 'y' && check != 'n'){
                //show the error
                System.out.println("You must type 'y' or 'n'!");
            }
        }

        //variable that will return if still calculating or no
        boolean still = true;

        //if the user answered y
        if(check == 'y') still = true; //still calculating
        //if the user answered n
        if(check == 'n') still = false; //still not calculating

        //return the still
        return still;
    }

    //method that resolves the calcule and shows the result
    static void calcule(double numOne, char op, double numTwo){ //receive the numbers and the operation as args
        //double that will receive the result
        double result = 0; 

        //switch..case that capture the operation and insert the correct calcule in result
        switch (op) {
            case '+': 
                result = numOne + numTwo;
                break;
            case '-':
                result = numOne - numTwo;
                break;
            case '*':
                result = numOne * numTwo;
                break;
            case '/':
                result = numOne / numTwo;
                break;
            case '%':
                result = numTwo * (numOne / 100);
                break;
        }

        //show the result
        System.out.printf("%2f %c %2f = %2f", numOne, op, numTwo, result);
    }
}