showFormBtn = document.getElementById("show-form");
bookingForm = document.getElementById("booking-form");

console.log(showFormBtn);

if(showFormBtn)
{
  showFormBtn.addEventListener("click", () => {
    bookingForm.style.display = "block";
  });
}