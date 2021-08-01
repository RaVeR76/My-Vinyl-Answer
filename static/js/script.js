// Declare Constants

const coll = document.getElementsByClassName("collapsible");
const password = document.getElementById("password");
const text = document.getElementById("caps-on");
let i;

$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });

});


//password.addEventListener("keyup", function(event) {

//    if (event.getModifierState("CapsLock")) {
//        text.style.display = "block";
//    } else {
//        text.style.display = "none"
//    }
//});





// collapsible JS taken from W3Schools

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        let content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}


// Taken from W3Schools for alerting when Caps Lock On at password input
password.addEventListener("keyup", function(event) {

    if (event.getModifierState("CapsLock")) {
        text.style.display = "block";
     } else {
        text.style.display = "none"
    }
});