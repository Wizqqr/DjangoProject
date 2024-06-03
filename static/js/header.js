// Smooth scroll to anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add slide-in animation to elements with 'slide-in' class
window.addEventListener('DOMContentLoaded', () => {
    const slideInElements = document.querySelectorAll('.slide-in');
    slideInElements.forEach(element => {
        element.classList.add('animate__animated', 'animate__fadeIn'); // Changed to fadeIn animation from Animate.css
    });
});

// Change navbar background color on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = '#212529'; // Darken background color on scroll
    } else {
        navbar.style.backgroundColor = '#343a40'; // Revert to original color
    }
});
