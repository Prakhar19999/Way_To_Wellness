// sub-navbar
const hamb = document.getElementById("hamb");
const navUL = document.getElementById("visible");
const hambicon = document.getElementById("subnav-icon");

hamb.addEventListener('click', () => {
    navUL.classList.toggle('show');
    hamb.classList.toggle('turn');
    hambicon.classList.toggle('change');
})