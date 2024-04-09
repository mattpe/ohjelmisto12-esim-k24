// JS mod 2 - Funktiot
// perinteinen function määritelmä
function doSomething() {
  console.log('doing something')
}
doSomething();

const doSomethingMore = () => {
  console.log('doing something else');
};
const result = doSomethingMore();
console.log(result);

const ages = [4, 55, 36];

// vertailufunktio sort()-metodia varten
function compare(val1, val2) {
  return val1 - val2;
}
console.log(compare(44, 33));
//ages.sort(compare);

// vertailufunktio nimettömänä funktiona
ages.sort(function (val1, val2) {
  return val1 - val2;
});
// vertailufunktio nuolifunktiona
ages.sort((val1, val2) => val1 - val2);
console.log(ages);

// tulostaa Arrayn sisällön ja palauttaa uuden taulukon käännetyssä järjestyksessä
function logArray(array) {
  // funktion sisällä esitelty muuttuja näkyy vain funktion sisällä
  //const ages = [];
  //console.log(ages);
  console.log(array);
  const newArray = array.slice(0);
  newArray.reverse();
  return newArray;
}

const reversedAges = logArray(ages);

console.log('orig ages', ages);
console.log('reversed', reversedAges);

// matskuesimerkki v2
function doLottery (numbers, num) {
  const row = [];
  while (row.length < num) {
    const r = Math.floor(Math.random() * numbers) + 1;
    if (!row.includes(r)) {
      row.push(r);
    }
  }
  return row.sort((a, b) => a-b);
}

const lottery = doLottery(40,7);
for (let i = 0; i < lottery.length; i++) {
    console.log(lottery[i]);
}