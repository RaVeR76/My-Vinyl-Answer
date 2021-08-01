// Declare Constants

const coll = document.getElementsByClassName("collapsible");



$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });

});



// collapsible JS taken from W3Schools
let i;
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


//$("img").on("error", function () {
//    $(this).attr("src", "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg");
//});