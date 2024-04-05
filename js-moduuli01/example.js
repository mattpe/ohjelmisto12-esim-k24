'use strict';

console.log('I have awaken!');

const name = 'Matti';
const names = ['Aku', 'Iines', 'Heluna'];

console.log('Moi ' + name);
console.log('tulostetaan kaikki nimet', name, names);

alert('Moi ' + name);
// alert('Toinen alertti');

const firstParagraphElement = document.querySelector('p');
console.log(firstParagraphElement);
firstParagraphElement.textContent = 'Moi ' + name;

const allParagraphElements = document.querySelectorAll('p');
console.log(allParagraphElements);
allParagraphElements[2].textContent = "kolmas tekstikappale";