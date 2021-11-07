let imgPopup = document.getElementsByClassName("img-clicked");

if(imgPopup)
{
  
  for(let i = 0; i < imgPopup.length; i++)
  {
    imgPopup[i].addEventListener("click", () => {
      popUp(i);
    });
  }
}

function popUp(n)
{
  // Creating elements
  let imgPopupContainer = document.createElement("div");
  let closeButtonSpanLeft = document.createElement("span");
  let closeButtonSpanRight = document.createElement("span");
  let img = document.createElement("img");
  // Initializing my new img
  img.src = imgPopup[n].src;
  // Appending the elements to the body
  document.body.appendChild(imgPopupContainer);
  imgPopupContainer.append(img, closeButtonSpanLeft, closeButtonSpanRight);
  //Creating the necessary classes and ids for scss
  imgPopupContainer.classList.add("img-popup-container");
  closeButtonSpanLeft.classList.add("close-button");
  closeButtonSpanLeft.id = "close-button-left";
  closeButtonSpanRight.id = "close-button-right";
  closeButtonSpanRight.classList.add("close-button");
  img.classList.add("img-popup");
  // Add event listener to close button
  closeButton = document.getElementsByClassName("close-button");
  if(closeButton)
  {
    for(var i = 0; i < closeButton.length; i++)
    {
      closeButton[i].addEventListener("click", () => {
        // Remove popUp
        document.body.removeChild(imgPopupContainer);
      });
    }
  }
}