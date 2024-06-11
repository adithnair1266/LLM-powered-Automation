function calculate() {
    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    var operation = document.getElementById("operation").value;

    var result = 0;

    switch (operation) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2;
            break;
        case "*":
            result = num1 * num2;
            break;
        case "/":
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                result = "Cannot divide by zero!";
            }
            break;
    }

    document.getElementById("result").innerHTML = "The result is: " + result;
}
