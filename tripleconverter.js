// exercice triple converter javascript

// creating the 3 functions

var eur = 1;
function convertChfEur(eur) {
    var chf = (eur / 1.03);
    return chf;
    }

var kg = 1;
function convertKgPound(kg) {
    var pound = (kg * 0.4);
    return pound;
    }

var litre = 1;
function convertLitreMetrescubes(litre) {
    var MetresCubes = (litre / 1000);
    return MetresCubes
}

var answer = window.prompt("Do you want to convert a value? (yes/no)");

while (answer == "yes"){
        var conv = window.prompt("Which conversion? (euros/kilos/litres)");
        if (conv == "euros"){
        eur = window.prompt("Which value do you want to convert?");
        console.log("The result is " + convertChfEur(eur));
        answer = window.prompt("Do you want to convert a value? (yes/no)");
        }
        else if (conv == "kilos"){
        kg = window.prompt("Which value do you want to convert?");
        console.log("The result is " + convertKgPound(kg));
        answer = window.prompt("Do you want to convert a value? (yes/no)");
        }
        else if (conv == "litres"){
        litre = window.prompt("Which value do you want to convert?");
        console.log("The result is " + convertLitreMetrescubes(litre));
        answer = window.prompt("Do you want to convert a value? (yes/no)");
        }
        else {
        window.prompt("Which value do you want to convert?");
        console.log("I cannot do this conversion!");
        }
}

