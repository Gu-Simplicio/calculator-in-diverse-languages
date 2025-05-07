import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        char operator;
        boolean stillCalc = true;
        double firstNumber, secondNumber;
        Scanner scanner = new Scanner(System.in);

        System.out.println("WELCOME TO JAVA CALCULATOR!");
        do{
            System.out.print("Insert the first number: ");
            firstNumber = scanner.nextDouble();

            operator = captureOperator(scanner);

            System.out.println("\nInsert the operation:");

            System.out.print("\nInsert the second number: ");
            secondNumber = scanner.nextDouble();

            calcule(firstNumber, operator, secondNumber);

            stillCalc = checkIfStillCalc(scanner);
        }while(stillCalc == true);
        System.out.print("Thanks for calculate!");
        scanner.close();
    }

    static char captureOperator(Scanner scanner){
        char opSelected = ' ';
        String[][] operations = {
            {"+", "sum"},
            {"-", "sub"},
            {"*", "mult"},
            {"/", "div"},
            {"%", "percent"}
        };

        do{
            for (int i = 0; i < operations.length; i++) {
                System.out.printf("type %s to %s\n", operations[i][0], operations[i][1]);
            }

            System.out.print("Insert your operation: ");
            opSelected = scanner.next().charAt(0);

            int aux = 0;
            for(int i = 0; i < operations.length; i++){
                if(opSelected != operations[i][0].charAt(0)) aux++;
            }
            if(aux == operations.length){
                System.out.print("\nInsert a correct operation!\n\n");
                opSelected = ' ';
            }
        }while(opSelected == ' ');
        return opSelected;
    }

    static boolean checkIfStillCalc(Scanner scanner){
        char check;
        System.out.print("\nDo you want to calculate again? [type 'y' or 'n']: ");
        check = scanner.next().charAt(0);

        while(check != 'y' && check != 'n'){
            System.out.print("\nDo you want to calculate again? [type 'y' or 'n']: ");
            check = scanner.nextLine().charAt(0);

            System.out.print(check == 'n');

            if(check != 'y' && check != 'n'){
                System.out.println("You must type 'y' or 'n'!");
            }
        }

        boolean still = true;

        if(check == 'y') still = true;
        if(check == 'n') still = false;

        return still;
    }

    static void calcule(double numOne, char op, double numTwo){
        double result = 0;

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

        System.out.printf("%2f %c %2f = %2f", numOne, op, numTwo, result);
    }
}