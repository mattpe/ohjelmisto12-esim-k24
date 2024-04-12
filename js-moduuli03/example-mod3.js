
function locationSuccess (location) {
  console.log('Käyttäjä paikannettu', location);
}

function locationError (error) {
  console.log('paikannus fail', error);
}

const locationOptions = {
  timeout: 5000
};

// käytetään tapahtumankäsittelijänä, kun p-näppäintä painetaan
function locateUser(event) {
  console.log('näppäintapahtuma', event);
  if (event.key === 'p') {
    navigator.geolocation.getCurrentPosition(locationSuccess, locationError, locationOptions);
  }
}

console.log('Moro!');

// DOM-kikkailua

const section2 = document.querySelectorAll('section')[1];
const pElement = section2.querySelector('p');
pElement.textContent = 'muokattu';

const newP = document.createElement('p');
newP.textContent = 'uusi kappale';
section2.append(newP);
// newP.style = 'color: blue';
newP.classList.add('blue');

const thirdSection = document.querySelector('#third-section');
thirdSection.innerHTML = `
    <h2>Kolmannen osion otsikko</h2>
    <p>
        Tässä taas tekstiä.
    </p>`;

// Tapahtumankäsittely

const buttonElement = document.querySelector('button');
buttonElement.addEventListener('click', function (event) {
  // pysäytetään click-eventin eteneminen dom-puussa tähän
  event.stopPropagation();
  console.log('button clicked');
  //newP.classList.add('red');
  //newP.classList.remove('blue');
  newP.classList.toggle('red');
  newP.classList.toggle('blue');
});

// näppäimistö
document.addEventListener('keypress', locateUser);

// hiiren liikutus
//document.addEventListener('mousemove', (event) => {
//  console.log(event);
//});

// kontekstimenun esto
document.addEventListener('contextmenu', function (event) {
  console.log(event);
  event.preventDefault();
  alert('ähäkutti!');
});

// tekstikappaleklikki
newP.addEventListener('click', function() {
  newP.textContent = 'paina p paikantaaksesi ';
});

// koko dokumentin klikkitapahtuma
document.addEventListener('click', function (event){
  console.log('sivua klikattu, kohde:', event.target, event.currentTarget.tagName);
  // klikkauksen kohde-elementin käsittely
  // event.target.textContent = 'klikkasit tätä';
  event.target.classList.toggle('red');
}, false);
