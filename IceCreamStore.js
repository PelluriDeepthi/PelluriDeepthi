// let sum = (a,b) =>{
//     console.log(a+b);
// }
// sum(4,5)
function verify() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "Delights" && password === "IceCream") {
        alert("Authentication successful!");
        window.location.href = "https://www.amazon.com";
    } else {
        alert("Authentication failed. Please check your credentials.");
    }
}
document.getElementById("sub").addEventListener("click", verify);