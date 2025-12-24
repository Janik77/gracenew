const header = document.querySelector(".site-header");
const burger = document.querySelector(".burger");
const nav = document.querySelector(".nav");

if (burger && nav) {
  burger.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    burger.setAttribute("aria-expanded", String(isOpen));
    if (header) {
      header.classList.toggle("menu-open", isOpen);
    }
  });
}
