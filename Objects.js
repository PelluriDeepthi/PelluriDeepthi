// Values assigning to keys are called properties. It contains key and values
const student = {
    firstName: 'Ram',
    class: 10
}
console.log(student);
console.log(typeof student);


// accessing property
console.log(student.firstName);    //using .

console.log(student["class"]);     //using []

// Nested Objects
const Person = {
    firstName: 'John',
    class: 10,
    marks:{
        Science: 70,
        Math: 75
    }
}
console.log("\n",Person.marks);
console.log(Person.marks.Math);

// Object Methods
const per = {
    name: 'Sam',
    age: 30,
    greet: function () {
        console.log('\nhi')
    }
}
per.greet();
console.log(per.name,per.age);

// Built-in Methods
let number = '23.32';
let result = parseInt(number);
let fresult = parseFloat(number);
console.log("\n",result);
console.log(fresult);

// using this keyword
const person = {
    name:'Krishna',
    age: 14,
    greet: function () {
        console.log('\nThe name is' + ' ' + this.name);
    }
}
person.greet();

// Literal is used to create a single object
// Constructor is used to create multiple objects
let personL = {
    name: 'Radha'
}


function PersonM() {
    this.name = 'Kahna'
}
let person1 = new PersonM();
console.log("\n",person1.name);


// prototype
function profun() {
    this.name = 'Kahna',
    this.age = 26
}
let perfun1 = new profun();
let perfun2 = new profun();

profun.prototype.gender = 'Male';         // Adding new property to constructor function
profun.prototype.area = 'Hyd';

console.log("\n",perfun1.gender);
console.log(perfun1.area);

// getter and setter
let Student = {
    firstname: 'Mohan',
    get getName(){                              //accessor property(getter)
        return this.firstname;
    }
}
console.log("\n",Student.firstname);            //accessing data property
console.log(Student.getName);                   //accessing getter methods
// console.log(Student.getName());                 //Trying to access the value as a method


let array = ["hello", "good evening"];
for (let i = 0; i < array.length; i++) {
    const element = array[i];
}
console.log("\nThe array is:",array);



let numb = 5;
if(numb==0){
    console.log(numb);
}
else if(numb>1 && numb<=10){
    console.log("\nIts a one digit number\n");
}
else if(numb>10 && numb<=20){
    console.log("\nIts a two digit number\n");
}
else{
    console.log("\nIts more than a two digit number\n")
}


// while condition
let a=2
while (a<9){
    console.log("The elements are:", a);
    a++;
}

