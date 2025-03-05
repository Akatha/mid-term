// Simple image slider for the home page
let currentSlide = 0;
const slides = document.querySelectorAll('.slider img');

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Automatically change slides every 5 seconds
setInterval(nextSlide, 5000);

// Show the first slide initially
showSlide(currentSlide);