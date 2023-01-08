function setCSSColourFile(darkmode) {
    let cssThemeTag = document.getElementById('theme');
    switch (darkmode) {
        case '0':
            cssThemeTag.href = cssThemeTag.href.replace(/(colours)|(light)|(dark)/g, "colours");
            break;
        case '1':
            cssThemeTag.href = cssThemeTag.href.replace(/(colours)|(light)|(dark)/g, "light");
            break;
        case '2':
            cssThemeTag.href = cssThemeTag.href.replace(/(colours)|(light)|(dark)/g, "dark");
            break;
    }
}

function readDarkModeSetting() {
    if (localStorage.getItem('darkmode')) {
        return localStorage.getItem('darkmode');
    } else {
        localStorage.setItem('darkmode', '0');
        return '0';
    }
}

let darkmode = readDarkModeSetting();
setCSSColourFile(darkmode);
