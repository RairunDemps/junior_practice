let dogName = "Gator"; // Global scope
// can use dogName here

// can use maleName here

// can't use carName here

function myFunction() {
    // can use dogName here

    let carName = "Volvo"; // Function scope
    // var carName = "Volvo";
    // const carName = "Volvo";

    maleName = "Jack";
    
    // can use carName here
}

// can use dogName here

// can use maleName here

// can't use carName here
