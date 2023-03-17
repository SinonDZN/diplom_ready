window.onload = function () {
    mybutton = document.getElementById('anchButton')
    mybutton.style.display = "none";
    window.onscroll = function () {
        scrollFunction()
    };
};


function scrollFunction() {
    if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
        mybutton.style.display = "block";
        mybutton.classList.add("btn-up");
    } else {
        mybutton.style.display = "none";
        mybutton.classList.remove("btn-up");

    }
}
