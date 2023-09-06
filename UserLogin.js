// Function to verify username and password
function verify() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "TechieBytes" && password === "India@123") {
        alert("Authentication successful!");
        window.location.href = "https://www.amazon.com";
    } else {
        alert("Authentication failed. Please check your credentials.");
    }
}

// Function to display rules
function show(elementId) {
    var element = document.getElementById(elementId);
    element.style.display = "block";
}

// Attach click event listener to the submit button
document.getElementById("sub").addEventListener("click", verify);

// Attach click event listener to the "Rules" button
document.getElementById("rule").addEventListener("click", function () {
    show("rules");
});
