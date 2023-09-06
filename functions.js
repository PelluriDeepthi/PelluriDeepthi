// Function declaration
function message() {
    console.log("\nHidden Castle");
}
message();


let showmessage = function() {
    console.log("\nPalm");
}
showmessage();


// arrow function
let myfunction = (a,b)=> a+b;
let resultfun = myfunction(4,5);
console.log("\n",resultfun,"\n");


let mul = (a,b)=> {
    return a*b;
}
mularray = mul(3,6);
console.log("\nThe multiplication of an array is:",mularray,"\n");



// Increments
for(let i=0;i<=5;i++){
    console.log("Array after Post increment:",i);
}

for(let i=0;i<=5;++i){
    console.log("Array after Pre increment:",i);
}

for(let i=3;i!=5;++i){
    console.log("Elements in arrray is:",i);
}

// This code doesn't run because we have given two initialisations i=0 and i=5 here
for(let i=0;i==5;i++){
    console.log(i);
}


// if-elseif-else
// number = 4
number = -12
// number = 0   //default variable
if (number<0) {
    console.log("\n",number,"is negative number")
}
else if(number>0){
    console.log("\n",number,"is positive number")
}
else{
    console.log("\n",number,"is a zero")
}

// Local and Global Variables
let globalVar = 10;

function localVarExample() {
    let localVar = 5;
    console.log("\nLocal variable number is:",localVar); // Accessing local variable
    console.log("Global variable number is:",globalVar); // Accessing global variable
}

localVarExample();
// console.log(localVar);



// Constructors
function person() {
    this.name = 'John';
    this.age = 23;
}
let person1 = new person();    //creating object
let person2 = new person();
console.log("\nName of a person:",person1.name);     //accessing properties
console.log("Age of a person is:",person2.age);


// Function in a Constructor function
function Person() {
    this.name = 'John';
    this.age = 23;
    this.greet = function () {
        console.log("hello");
    }
}
let Person1 = new Person();    //creating object
let Person2 = new Person();
console.log("\nName of a person:",Person1.name);     //accessing properties
console.log("Age of a person is:",Person2.name);


function newPerson(newname,newage,newcity) {
    this.name = newname;
    this.age = newage;
    this.city = newcity;
    this.greet = function (greeting) {
        this.greeting = greeting;
        return greeting;
        // we have to use only one return statement in a function
        // console.log("hello");
    }
}
let newPerson1 = new newPerson("Vaishu",25,"Hyd");
let newPerson2 = new newPerson("Deepu",26,"Guntur");
console.log("\nDetails of person 1 is:",newPerson1.name, newPerson1.age, newPerson1.city, newPerson1.greet("Hello"));
console.log("Details of person 2 is:",newPerson2.name, newPerson2.age, newPerson2.city, newPerson2.greet("Hi"));


function newperson(newname,newage,newcity,greet) {
    this.name = newname;
    this.age = newage;
    this.city = newcity;
    this.greet = function () {
        if (this.name === "Deepu") {
            return ("Hello");
        }
        else{
            return ("hi");
        }
        
        // we have to use only one return statement in a function
        // console.log("hello");
    }
}
let newperson1 = new newperson("Vaishu",25,"Hyd");
let newperson2 = new newperson("Deepu",26,"Guntur");
console.log("\nDetails of person 1 is:",newperson1.name, newperson1.age, newperson1.city, newperson1.greet());
console.log("Details of person 2 is:",newperson2.name, newperson2.age, newperson2.city, newperson2.greet());
