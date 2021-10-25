var checkoutButton = document.querySelector('#checkout-button');

fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  if(checkoutButton)
  {
    checkoutButton.addEventListener('click', function() {
      fetch("/create-checkout-session/")
      .then((result) => 
        { 
          return result.json();
        })
        .then((data) => 
        {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({sessionId: data.sessionId})
        })
        .then((res) => 
        {
          console.log(res);
        });
    });
  }
});
