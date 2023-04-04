function validateForm() {
    var name = document.forms["myForm"]["name"].value;
    var email = document.forms["myForm"]["email"].value;
    var message = document.forms["myForm"]["message"].value;
  
    if (name == "") {
      document.getElementById("errorname").innerHTML = "Veuillez saisir votre nom.";
      return false;
    }
  
    if (email == "") {
      document.getElementById("erroremail").innerHTML = "Veuillez saisir votre adresse e-mail.";
      return false;
    }
  
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      document.getElementById("erroremail").innerHTML = "Veuillez saisir une adresse e-mail valide.";
      return false;
    }
  
    if (message == "") {
      document.getElementById("errormsg").innerHTML = "Veuillez saisir votre message.";
      return false;
    }
  
    return true;
  }