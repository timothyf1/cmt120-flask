let darkmode = 0

if (!localStorage.getItem('darkmode')) {
    localStorage.setItem('darkmode', darkmode);
} else {
    let darkmode = localStorage.getItem('darkmode')
}

let cssThemeTag = document.getElementById('theme')

switch (darkmode) {
    case 1:
        cssThemeTag.href = cssThemeTag.href.replace("colours", "light")
        break;
    case 2:
        cssThemeTag.href = cssThemeTag.href.replace("colours", "dark")
        break;
}
