showFormBtn = document.getElementById("show-form");
bookingForm = document.getElementById("form-container");

console.log(showFormBtn);

if(showFormBtn)
{
  showFormBtn.addEventListener("click", () => {
    bookingForm.style.display = "block";
  });
}