// Generate a random arithmetic equation
function generateCaptcha() {
    const num1 = Math.floor(Math.random() * 10) + 1;
    const num2 = Math.floor(Math.random() * 10) + 1;
    return `${num1} + ${num2}`;
}

// Check if the user's answer is correct
function verifyCaptcha(answer) {
    const equation = document.getElementById('captcha-equation').textContent;
    const parts = equation.split('+');
    const expectedAnswer = parseInt(parts[0]) + parseInt(parts[1]);
    return answer === expectedAnswer.toString();
}

document.addEventListener('DOMContentLoaded', () => {
    const equationElement = document.getElementById('captcha-equation');
    const resultElement = document.getElementById('captcha-result');
    const submitButton = document.getElementById('captcha-submit');

    submitButton.addEventListener('click', () => {
        const userAnswer = document.getElementById('captcha-input').value;
        if (verifyCaptcha(userAnswer)) {
            resultElement.textContent = 'Captcha passed! You are human.';
        } else {
            resultElement.textContent = 'Captcha failed. Please try again.';
            equationElement.textContent = generateCaptcha();
        }
    });

    equationElement.textContent = generateCaptcha();
});

let name_string = "nani";
let age_numaic = 22;
const phoneNumber_numaric = 9912542198;
let grade_float = 8.4;

let x= 10
if (x=10){
    console.log(true)
}
else{
    console.log(false)
}


















