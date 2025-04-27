class Calculator{
    constructor(){
        this.count = 0;
        this.countToShow = "0";
        this.labelCount = document.querySelector("#labelCount");
        this.resultInput = document.querySelector("#resultInput");

        setInterval(() => {
            if(this.countToShow == "") this.countToShow = "0";

            this.resultInput.value = this.countToShow;

            if(this.countToShow == "0"){
                document.querySelector("#showResultInput").disabled = true;
            } else {
                document.querySelector("#showResultInput").disabled = false;
            }
        }, 100)
    }

    addNumber(number){
        this.countToShow == "0" ? this.countToShow = number : this.countToShow += number;
    }
    addPoint(point){
        if(!this.countToShow.includes(point)) {
            this.countToShow == "" ? this.countToShow += `0${point}` : this.countToShow += point;
        }
    }
    addOperation(op){
        if(op == "-" && this.countToShow == "0") this.countToShow = "-"

        if(this.countToShow != "0"){
            if(this.count != 0){    
                let lastCount = this.labelCount.textContent.split("");
                lastCount = lastCount[lastCount.length - 1];

                switch(lastCount){
                    case "+":
                        this.count = this.count + Number(this.countToShow);
                        break;
                    case "-":
                        this.count = this.count - Number(this.countToShow);
                        break;                        
                    case "*":
                        this.count = this.count * Number(this.countToShow);
                        break;
                    case "/":
                        this.count = this.count / Number(this.countToShow);
                        break;
                    case "%":
                        this.count = Number(this.countToShow) * (this.count / 100);
                        break;
                }
            } else {
                this.count = Number(this.countToShow);
            }

            this.countToShow = "";
            this.labelCount.textContent = `${this.count} ${op}`
        } else {
            let test = this.labelCount.textContent.split("");
            test.pop();
            test.push(op);
            this.labelCount.textContent = test.toString("").replace(/,/g, "")            
        }
    }

    showResult(){
        let lastCount = this.labelCount.textContent.split("");
        lastCount = lastCount[lastCount.length - 1];
        this.addOperation(lastCount)

        this.labelCount.textContent = "";
        this.countToShow = this.count
    }

    removeOne(){
        if(this.countToShow != "0"){
            let charsCount = this.countToShow.split("");
            charsCount.pop();
            this.countToShow = charsCount.toString().replace(/,/g, "");
        }
    }

    clearAll(){
        this.countToShow = "0";
    }
}

let calculator = new Calculator();