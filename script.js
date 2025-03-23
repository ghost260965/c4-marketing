// Explosive Animations for Hero Text
gsap.from(".explode-text", { duration: 1.5, scale: 0, ease: "bounce.out" });

// Smooth scrolling effect
document.querySelector('.cta-button').addEventListener('click', function(event) {
    event.preventDefault();
    document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
});

// Service Cards Hover Effects
document.querySelectorAll(".service").forEach(service => {
    service.addEventListener("mouseenter", () => {
        gsap.to(service, { scale: 1.15, duration: 0.3, boxShadow: "0 0 20px red" });
    });
    service.addEventListener("mouseleave", () => {
        gsap.to(service, { scale: 1, duration: 0.3, boxShadow: "none" });
    });
});
