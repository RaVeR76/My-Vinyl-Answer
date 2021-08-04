// Declare Constants

const coll = document.getElementsByClassName("collapsible");
//const password = document.getElementById("password");
//const text = document.getElementById("caps-on");
const genre = document.getElementById("admin_genre");
const genre_select = document.getElementById("genre_select");
const addGenre = document.getElementById("add_genre");
const editGenre = document.getElementById("edit_genre");
const genre_input = document.getElementById("genre_input");


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

    genre_input.style.display = "none";
    genre_select.style.display = "block";
    genre_select.innerHTML = genre.value;

};


function genreAdd() {

    genre_input.value = "";
    genre_input.placeholder = "Add New Genre Here";
    genre_input.style.display = "block";
    genre_select.style.display = "none";
    

};


function genreEdit() {

    genre_input.value = genre.options[genre.selectedIndex].text;
    genre_input.style.display = "block";
    genre_select.style.display = "none";
};


//function capsOn(event) {

  //  event.preventDefault();
    
   //     if (event.getModifierState("CapsLock")) {
   //         text.style.display = "block";
    //    } else {
    //        text.style.display = "none";
    //    };
//};

//password.addEventListener("keyup", capsOn); 
editGenre.addEventListener("click", genreEdit);
genre.addEventListener("change", genreChoice);
addGenre.addEventListener("click", genreAdd);
//editGenre.addEventListener("click", genreEdit);


//password.addEventListener("keyup", capsOn);