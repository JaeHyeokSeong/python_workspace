const toggleButton = document.querySelector('.navbar_toggleButton');
const menu = document.querySelector('.navbar_menu');
const login = document.querySelector('.navbar_login');

toggleButton.addEventListener('click', () => {
    menu.classList.toggle('active');
    login.classList.toggle('active');
});


