let header = document.getElementsByTagName("header")[0];
let headerStyle = getComputedStyle(header);
let resetHeight = headerStyle.marginTop.replace(/[^0-9.]/g, '');
let stickyHeight = header.offsetTop;
let breadcrumbs = document.getElementsByClassName("breadcrumb")[0];

// JS function to add and remove class
// This code was adapted from w3schools - How TO - Sticky/Affix Navbar
// accessed on 2023-01-05
// https://www.w3schools.com/HOWTO/howto_js_navbar_sticky.asp
window.onscroll = () => {
    if (window.pageYOffset > stickyHeight) {
        header.classList.add("sticky");
        breadcrumbs.classList.add("sticky-pad");
    }
    if (window.pageYOffset <= resetHeight) {
        header.classList.remove("sticky");
        breadcrumbs.classList.remove("sticky-pad");
    }
}
/* end of referenced code */
