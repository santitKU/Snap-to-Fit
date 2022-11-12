const h = document.querySelector(".hamburger");
const n = document.querySelector(".nav");

h.addEventListener("click", () => {
    n.classList.toggle("open");
})



const numb = document.querySelector(".numb");
let counter = 0;
setInterval(() => {
    if (counter == 60) {
        clearInterval();
    } else {
        counter += 1;
        numb.textContent = counter + "%";
    }
}, 80);