const cars = ["Saab", "Volvo", "BMW"];

const carsExplicit = new Array("Saab", "Volvo", "BMW");

MyObject = {"name": "Jack", "age": 12}
HululaObject = {"myObject": MyObject}

document.getElementById("demo").innerHTML =
cars + " " + HululaObject["myObject"]["name"]
