// Declare Constants

const coll = document.getElementsByClassName("collapsible");
const password = document.getElementById("password");
const text = document.getElementById("caps-on");
const genre = document.getElementById("admin_genre");
let i;


$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });

});


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
};


//const passwordRef = document.querySelector('#password');
//const capsOnRef = document.querySelector('#caps-on');
//const genreRef = document.querySelector('#admin_genre');
//const srtRef = document.querySelector('#srt');



//function callMeWhatYouWAnt(event) {
//  event.preventDefault();
//  if (event.getModifierState('CapsLock')) {
//    text.style.display = 'block';
//  } else {
//    text.style.display = 'none';
//  }
//  srtRef.innerHTML = genreRef.value;
//};


//password.addEventListener('keyup', callMeWhatYouWAnt);
//genre.addEventListener('change', callMeWhatYouWAnt);








// Taken from W3Schools for alerting when Caps Lock On at password input
//password.addEventListener("keyup", function(event) {
//
//    if (event.getModifierState("CapsLock")) {
//        text.style.display = "block";
//     } else {
//        text.style.display = "none";
//    }
//});


function genreChoice(event) {

    event.preventDefault();

        document.getElementById("genre_select").innerHTML = document.getElementById("admin_genre").value;
    
    };


function capsOn(event) {

    event.preventDefault();
    
        if (event.getModifierState("CapsLock")) {
            text.style.display = "block";
        } else {
            text.style.display = "none";
        };
};

//password.addEventListener("keyup", capsOn); 
genre.addEventListener("change", genreChoice);
password.addEventListener("keyup", capsOn);