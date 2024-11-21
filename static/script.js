document.addEventListener("DOMContentLoaded", function () {
  const elements = document.querySelectorAll(
    "#mainImage, #projectTitle, .card-container p, #secondaryImagesContainer img"
  );

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.style.animationPlayState = "running";
        }
      });
    },
    { threshold: 0.1 }
  );

  elements.forEach((el) => {
    el.style.animationPlayState = "paused"; // Pause animations initially
    observer.observe(el);
  });
});
