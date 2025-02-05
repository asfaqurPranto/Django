const menuBtn = document.getElementById('menu-btn');

const mobileMenu = document.getElementById('mobile-menu');
const closeMenu = document.getElementById('close-btn');
const body = document.getElementById('body');
const menuLi = document.querySelectorAll('.menu-link');
const introCard = document.getElementById('intro-card');

menuBtn.addEventListener('click', () => {
  mobileMenu.classList.remove('hidden');
  body.style.overflow = 'hidden';
  introCard.style.visibility = 'hidden';
  menuBtn.style.visibility = 'hidden';
});

closeMenu.addEventListener('click', () => {
  mobileMenu.classList.add('hidden');
  body.style.overflow = 'visible';
  introCard.style.visibility = 'visible';
  menuBtn.style.visibility = 'visible';
});

for (let i = 0; i < menuLi.length; i++) {
  menuLi[i].addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
    body.style.overflow = 'visible';
    introCard.style.visibility = 'visible';
    menuBtn.style.visibility = 'visible';
  });
}

const professionalArray = [
  {
    image: './img/profile-icon.svg',
    name: 'Shiakh Hossain',
    occupation: 'Business Advisor',
    description: "Experienced business advisor offering strategic guidance and expertise to entrepreneurs and organizations. Specializing in helping businesses scale, optimize operations, and achieve long-term success.",
  },
  {
    image: './img/profile-icon.svg',
    name: 'Shiakh Hossain',
    occupation: 'Business Advisor',
    description: "Experienced business advisor offering strategic guidance and expertise to entrepreneurs and organizations. Specializing in helping businesses scale, optimize operations, and achieve long-term success.",
  },
  {
    image: './img/profile-icon.svg',
    name: 'Shiakh Hossain',
    occupation: 'Business Advisor',
    description: "Experienced business advisor offering strategic guidance and expertise to entrepreneurs and organizations. Specializing in helping businesses scale, optimize operations, and achieve long-term success.",
  },
  {
    image: './img/profile-icon.svg',
    name: 'Shiakh Hossain',
    occupation: 'Business Advisor',
    description: "Experienced business advisor offering strategic guidance and expertise to entrepreneurs and organizations. Specializing in helping businesses scale, optimize operations, and achieve long-term success.",
  },
  {
    image: './img/profile-icon.svg',
    name: 'Shiakh Hossain',
    occupation: 'Business Advisor',
    description: "Experienced business advisor offering strategic guidance and expertise to entrepreneurs and organizations. Specializing in helping businesses scale, optimize operations, and achieve long-term success.",
  },
  {
    image: './img/profile-icon.svg',
    name: 'Shiakh Hossain',
    occupation: 'Business Advisor',
    description: "Experienced business advisor offering strategic guidance and expertise to entrepreneurs and organizations. Specializing in helping businesses scale, optimize operations, and achieve long-term success.",
  },
];

const professionalList = document.getElementById('professional-list');

function displayProfessional(professionalID) {
  professionalList.innerHTML += `
  <li>
  <div class="card d-flex flex-row">
    <img
      class="professional-img align-self-center"
      src="${professionalArray[professionalID].image}"
      alt="${professionalArray[professionalID].name} image"
    />
    <div class="card-body">
      <h4 class="card-title">${professionalArray[professionalID].name}</h4>
      <p class="card-text primary-color">
      ${professionalArray[professionalID].occupation}
      </p>
      <div class="short-grey-line"></div>
      <p class="card-text secondary-color">
      ${professionalArray[professionalID].description}
      </p>
    </div>
  </div>
</li>
  `;
}

for (let i = 0; i < professionalArray.length; i++) {
  displayProfessional(i);
}