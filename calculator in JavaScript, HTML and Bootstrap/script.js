class Calculator{
    constructor(){
        this.count = "0";
        this.resultInput = document.querySelector("#resultInput");

        setInterval(() => {
            this.resultInput.value = this.count;

            if(this.count == "0" || this.count == ""){
                document.querySelector("#showResultInput").disabled = true;
            } else {
                document.querySelector("#showResultInput").disabled = false;
            }
        }, 100)
    }

    addNumber(number){
        this.count == "0" ? this.count = number : this.count += number;
    }
    addComma(comma){
        if(!this.count.includes(comma)) {
            this.count == "" ? this.count += `0${comma}` : this.count += comma;
        }
    }

    removeOne(){
        let charsCount = this.count.split("");
        charsCount.pop();
        this.count = charsCount.join("").toString()
    }

    clearAll(){
        this.count = "0";
    }
}

let calculator = new Calculator();