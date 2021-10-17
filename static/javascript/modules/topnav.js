var hamburgerMenu = document.querySelector(".hamburger");
var navMenu = document.querySelector(".nav__links");
const navLink = document.querySelectorAll(".nav__link");

if(hamburgerMenu)
{
    hamburgerMenu.addEventListener("click", toggleMobileMenu);
}

export function toggleMobileMenu()
{
    hamburgerMenu.classList.toggle("is__active");
    navMenu.classList.toggle("is__active");
}

if(navLink)
{
    navLink.forEach(n => n.addEventListener("click", closeMenu));
}

export function closeMenu()
{
    hamburgerMenu.classList.remove("is__active");
    navMenu.classList.remove("is__active");
}