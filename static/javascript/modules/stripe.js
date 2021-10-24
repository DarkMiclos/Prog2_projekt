var stripe = Stripe('{{ stripe_publishable_key }}');
var checkoutButton = document.getElementById('checkout-button');
if(checkoutButton)
{
  checkoutButton.addEventListener('click', function() {
    fetch("{% url 'create_checkout_session' id=object.id %}")
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
