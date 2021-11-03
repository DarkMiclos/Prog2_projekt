let slideIndex = 1;
let duration = 4000;
let previousSlide = document.getElementById("previous-slide");
let nextSlide = document.getElementById("next-slide");
let bars = document.getElementsByClassName("slide-bar");
let slides = document.getElementsByClassName("slides");

console.log(bars);

showSlide(slideIndex);

if(previousSlide)
{
  previousSlide.addEventListener("click", () => {
    showPreviousSlide();
    clearInterval(interval);
    interval = setInterval(function () {
      autoSlideShow();
    }, duration);
  });
}

if(nextSlide)
{
  nextSlide.addEventListener("click", () => {
    showNextSlide();
    clearInterval(interval);
    interval = setInterval(function () {
      autoSlideShow();
    }, duration);
  });
}

if(bars)
{
  for(let i = 0; i < bars.length; i++)
  {
    bars[i].addEventListener("click", () => {
      slideIndex = 1;
      slideIndex += i;
      showSlide(slideIndex);
      clearInterval(interval);
      interval = setInterval(function () {
        autoSlideShow();
      }, duration);
    });
  }
}

function showNextSlide()
{
  slideIndex++;
  showSlide(slideIndex);
}

function showPreviousSlide()
{
  slideIndex--;
  showSlide(slideIndex);
}

function hideAllImages()
{
  for(let i = 0; i < slides.length; i++)
  {
    slides[i].style.display = "none";
    bars[i].classList.remove("active");
  }
}

function displaySlide(n)
{
  if(n < 1)
  {
    slideIndex = slides.length;
  }
  if(n > slides.length)
  {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";
  bars[slideIndex - 1].classList.add("active");
}

function showSlide(n)
{
  hideAllImages();
  displaySlide(n);
}

function autoSlideShow()
{
  slideIndex += 1;
  hideAllImages();
  displaySlide(slideIndex);
}

let interval = setInterval(function () {
  autoSlideShow();
}, duration);