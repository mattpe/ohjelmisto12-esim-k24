
function locationSuccess (location) {
  console.log('Käyttäjä paikannettu', location);
}

function locationError (error) {
  console.log('paikannus fail', error);
}

const locationOptions = {
  timeout: 3000
};

navigator.geolocation.getCurrentPosition(locationSuccess, locationError, locationOptions);
console.log('Moro!');

// DOM-kikkailua

const section2 = document.querySelectorAll('section')[1];
const pElement = section2.querySelector('p');
pElement.textContent = 'muokattu';

const newP = document.createElement('p');
newP.textContent = 'uusi kappale';
section2.append(newP);
newP.style = 'color: blue';

const thirdSection = document.querySelector('#third-section');
thirdSection.innerHTML = `
    <h2>Kolmannen osion otsikko</h2>
    <p>
        Tässä taas tekstiä.
    </p>`;
