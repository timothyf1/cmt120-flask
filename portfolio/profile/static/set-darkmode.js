let darkmodeField = document.getElementById('darkmode');

function setDarkMode(value) {
    localStorage.setItem('darkmode', value);
    console.log(localStorage.getItem('darkmode'))
    setCSSColourFile(`${value}`)
}
