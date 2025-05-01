//create the class of the calculator
class Calculator{
    //constructor of the class
    constructor(){
        //count that will be made
        this.count = 0;
        //count that will be show
        this.countToShow = "0";
        //capture the element of the label
        this.labelCount = document.querySelector("#labelCount");
        //capture the element of the result input
        this.resultInput = document.querySelector("#resultInput");

        //set a interval that write correctly the numbers in the calculator
        setInterval(() => {
            //if the user remove all numbers, show the number 0
            if(this.countToShow == "") this.countToShow = "0";

            //the resultInput will show the countToShow
            this.resultInput.value = this.countToShow;
            
            //if the countToShow's equal 0
            if(this.countToShow == "0"){
                //the input that show the result is disabled
                document.querySelector("#showResultInput").disabled = true;
            } else { //if isn't
                //the input that show the result is enabled
                document.querySelector("#showResultInput").disabled = false;
            }
        }, 100) //the interval occours every 100 miliseconds
    }

    //method that add a number in the countToShow
    addNumber(number){
        //if the countToShow is equal 0, become the number, if isn't, add the number
        this.countToShow == "0" ? this.countToShow = number : this.countToShow += number;
    }

    //method that add the point
    addPoint(point){
        //if has'nt any point in the countToShow
        if(!this.countToShow.includes(point)) {
            //add a point, checking if already has something in or not
            this.countToShow == "" ? this.countToShow += `0${point}` : this.countToShow += point;
        }
    }

    //methid that add an operation in the count
    addOperation(op){
        //instance a negative number if the countToShow < 1
        if(op == "-" && (this.countToShow == "0" || this.countToShow == "")) this.countToShow = "-"

        //if the countToShow isn't 0
        if(this.countToShow != "0" && this.countToShow != "-"){
            //if the count is diferent than 0
            if(this.count != 0){    
                //capture the counts inserted
                let lastCount = this.labelCount.textContent.split("");
                //capture just the last count
                lastCount = lastCount[lastCount.length - 1];

                //switch..case to insert the correct operation in the countToShow
                switch(lastCount){
                    //if is the sum operation
                    case "+":
                        //sum the numbers already inserted with the numbers in the countToShow
                        this.count = this.count + Number(this.countToShow);
                        break;
                    //if is the subtraction operation
                    case "-":
                        //subtract the numbers already inserted with the numbers in the countToShow
                        this.count = this.count - Number(this.countToShow);
                        break;    
                    // if is the multiplication operation                     
                    case "*":
                        //multiply the numbers already inserted with the numbers in the countToShow
                        this.count = this.count * Number(this.countToShow);
                        break;
                    //if is the division operation 
                    case "/":
                        //divides the numbers already inserted with the numbers in the countToShow
                        this.count = this.count / Number(this.countToShow);
                        break;
                    //if is a percentabe
                    case "%":
                        //calculate the percent of the number in countToShow of the count inserted
                        this.count = Number(this.countToShow) * (this.count / 100);
                        break;
                }
            } else { //if countToShow == 0
                //count 
                this.count = Number(this.countToShow);
            }
            
            //transfomr countToShow in 0
            this.countToShow = "";
            //add the count in the label
            this.labelCount.textContent = `${this.count} ${op}`
        } else { //if countToShow == 0
            if(this.labelCount.textContent != ""){ //if has something in the labelCount
                //create a array with the counts in labelCount
                let correctCount = this.labelCount.textContent.split("");
                correctCount.pop(); //remove the last operation
                correctCount.push(op); //insert the new operation
                //show the new count
                this.labelCount.textContent = correctCount.toString("").replace(/,/g, "")  
            } 
        }
    }

    //method that show the result of the count   
    showResult(){
        //create an array with the data in labelCount
        let lastCount = this.labelCount.textContent.split("");
        //capture the lastCount (last index of the array)
        lastCount = lastCount[lastCount.length - 1];
        //active the method addOperation
        this.addOperation(lastCount)

        //clear the labelCount
        this.labelCount.textContent = "";
        //insert the count in countToShow
        this.countToShow = this.count;
    }

    //method that remove the last charactere in countToShow
    removeOne(){
        //if countToShow has anything
        if(this.countToShow != "0"){
            //capture all the chars of countToShow in an array
            let charsCount = this.countToShow.split(""); 
            charsCount.pop(); //remove the last one
            this.countToShow = charsCount.toString().replace(/,/g, ""); //reset countToShow
        }
    }
    
    //method that clear the calculator
    clearAll(){
        //reset all the attributes
        this.count = 0;
        this.countToShow = "0";
        this.labelCount.textContent = "";
    }
}
//start a new Calculator
let calculator = new Calculator();