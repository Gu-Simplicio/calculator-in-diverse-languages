import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        boolean stillPlaying = true;
        double firstNumber, secondNumber;
        Scanner scanner = new Scanner(System.in);

        System.out.println("WELCOME TO JAVA CALCULATOR!");
        do{
            System.out.print("Insert the first number: ");
            firstNumber = scanner.nextDouble();

            System.out.println(captureOp(scanner));

            System.out.println("\nInsert the operation:");

            System.out.print("\nInsert the second number: ");
            secondNumber = scanner.nextDouble();

            System.out.printf("%2f + %2f == %2f", firstNumber, secondNumber, firstNumber + secondNumber);
        }while(stillPlaying == true);

        scanner.close();
    }

    static char captureOp(Scanner scanner){
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
                opSelected = ' ';
            }
        }while(opSelected == ' ');
        return opSelected;
    }
}

