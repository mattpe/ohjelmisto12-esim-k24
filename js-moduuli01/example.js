'use strict';

console.log('I have awaken!');

let name = 'Matti';
const names = ['Aku', 'Iines', 'Heluna'];

let age, height;
age = 5.1;
console.log(age, typeof age, height, typeof height);

// muutetaan number -> string
age = age.toString();
console.log(age);
// muutetaan string -> number
// age = parseInt(age); // ottaa vaan kokonaisosan
age = parseFloat(age);
console.log(age, typeof age);
const ageAdd = 3;

// lisätään arvoon 1
age++;
// sama
// age = age + 1;
// age += 1;

console.log(age + ageAdd);

console.log(name + 'n ikä on ' + age + ' vuotta.');
// sama template stringillä:
console.log(`${name}n ikä on ${age} vuotta.`);

const isUnderAge = true;
console.log(isUnderAge, typeof isUnderAge)

console.log('Moi ' + name, typeof name);
console.log('tulostetaan kaikki nimet', name, names);

//alert('Moi ' + name);
// alert('Toinen alertti');

// haetaan viittaus ensimmäiseen p-elementtiin
const firstParagraphElement = document.querySelector('p');
console.log(firstParagraphElement);
// muutetaan p:n tekstisisältöä
firstParagraphElement.textContent = 'Moi ' + name;

const allParagraphElements = document.querySelectorAll('p');
console.log(allParagraphElements);
allParagraphElements[2].textContent = "kolmas tekstikappale";

name = 'Aku';

// syötteen lukeminen suoraan JS
// name = prompt('Anna nimi');
// console.log(name, typeof name);

// Math
console.log(Math.random())

// arvotaan kokonaislukuna arvo väliltä 1-6
console.log(Math.floor(Math.random()*6+1))




