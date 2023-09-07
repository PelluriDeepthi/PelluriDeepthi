// getter and setter
let Student = {
    firstname: 'Mohan',
    get getName(){                              //accessor property(getter)
        return this.firstname;
    }
}
console.log("\n",Student.firstname);            //accessing data property
console.log(Student.getName);                   //accessing getter methods
// console.log(Student.getName());  


let student = {
    firstname: 'Govind',
    set changeName(newName){                    //accessor property(setter)
        this.firstname = newName;
    }
}
console.log("\n",student.firstname);            
student.changeName = 'Madhan';                 //change(set) object property using a setter
console.log(student.firstname);       
  


  let Person= {
    firstname: 'Lalla',
    id: 78,
    isperson: true,
    /**
     * @param {number} newid
     */
    set changeid(newid){
        this.id = newid;
    }
  }
  console.log('\nStudent id is:',Person.id)
  console.log('Student is:',Person.isperson)
  Person.id = 87;
  console.log('Student new id is:',Person.id)



  // Define an object with a property and a setter for validation
const product = {
    _price: 0, // Private property (convention: prefix with an underscore)
    
    // Define a setter for the price property
    set price(newPrice) {
      if (typeof newPrice === 'number' && newPrice >= 0) {
        this._price = newPrice; // Set the price if it's a non-negative number
      } else {
        console.error('Invalid price value'); // Log an error for invalid input
      }
    },
  
    // Define a getter to retrieve the price
    get price() {
      return this._price;
    }
  };
  
  // Set the price using the setter
  product.price = 25; // Valid input
  
  // Try to set an invalid price
  product.price = 10; // Invalid input, will log an error
  
  // Get the price using the getter
  console.log('\nProduct Price:', product.price); // Output: Product Price: 25



  const car = {
    name: 'Audi',
    model: 'Q6',
    year: 2022,
    get carname(){
        return this.name+" "+this.model+" "+this.year;
    },
    set updatemodel(_newmodel){
        this.model = _newmodel;
    },
    set updateyear(_newyear){
        this.year = _newyear;
    }
  }
  console.log("\nCar details are:",car.name, car.model, car.year)
  car.updatemodel = 'Q8';
  car.updateyear = '2023';
  console.log("Updated Car details are:",car.name, car.model, car.year)