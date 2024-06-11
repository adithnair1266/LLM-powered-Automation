function findFactorial() {
    let num = parseInt(prompt("Enter a number:"));
    let result = 1;

    for (let i = 1; i <= num; i++) {
        result *= i;
    }

    alert(`The factorial of ${num} is ${result}`);
}

findFactorial();