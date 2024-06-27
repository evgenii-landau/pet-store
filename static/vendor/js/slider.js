let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = Math.ceil(slides.length / 4);

document.getElementById('pagination').innerHTML = Array(totalSlides).fill().map((_, i) => `<span class="dot ${i === 0 ? 'active' : ''}" onclick="goToSlide(${i})"></span>`).join('');

function updateSlidePosition() {
    const slider = document.getElementById('slider');
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
    document.querySelectorAll('.dot').forEach((dot, index) => {
        dot.classList.toggle('active', index === currentSlide);
    });
}

function nextSlide() {
    if (currentSlide < totalSlides - 1) {
        currentSlide++;
    } else {
        currentSlide = 0;
    }
    updateSlidePosition();
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
    } else {
        currentSlide = totalSlides - 1;
    }
    updateSlidePosition();
}

function goToSlide(slideIndex) {
    currentSlide = slideIndex;
    updateSlidePosition();
}
