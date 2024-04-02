document.addEventListener('DOMContentLoaded', function () {
    const navbarToggler = document.querySelector('.navbar-toggler-icon');
    const navbarLinks = document.querySelector('.navbar .links');

    navbarToggler.addEventListener('click', function () {
        navbarLinks.classList.toggle('show-menu');
    });
});
// JavaScript for toggle switch functionality
$(document).ready(function() {
    $('.switch input').change(function() {
        // Toggle the background color of the slider
        if ($(this).is(':checked')) {
            $(this).next('.slider').css('background-color', '#2196F3');
        } else {
            $(this).next('.slider').css('background-color', '#a59898');
        }
    });
});
