window.onload = function() {
    var hamburgerMenu = document.querySelector(".hamburger");
    var navMenu = document.querySelector(".nav__links");

    if(hamburgerMenu)
    {
        hamburgerMenu.addEventListener("click", mobileMenu);
    }
    

    function mobileMenu() {
        hamburgerMenu.classList.toggle("is__active");
        navMenu.classList.toggle("is__active");
    }
}