const images = [
    "/static/core/images/tech-1.jpg",
    "/static/core/images/tech-2.jpg",
    "/static/core/images/tech-3.jpg"
];

let currentSlide = 0;

const hero = document.querySelector(".hero");
const dots = document.querySelectorAll(".slide-dot");

function changeSlide() {

    currentSlide++;

    if (currentSlide >= images.length) {
        currentSlide = 0;
    }

    hero.style.backgroundImage = `url("${images[currentSlide]}")`;

    dots.forEach((dot, index) => {
        dot.classList.toggle("active", index === currentSlide);
    });
}

setInterval(changeSlide, 6000);