function setCSSColourDarkMode(darkmode) {
    let cssThemeTag = document.getElementById('theme');
    switch (darkmode) {
        case '0':
            cssThemeTag.href = cssThemeTag.href.replace(/(system)|(light)|(dark)/g, "system");
            break;
        case '1':
            cssThemeTag.href = cssThemeTag.href.replace(/(system)|(light)|(dark)/g, "light");
            break;
        case '2':
            cssThemeTag.href = cssThemeTag.href.replace(/(system)|(light)|(dark)/g, "dark");
            break;
    }
}

function setCSSAccessMode(access) {
    let cssThemeTag = document.getElementById('theme');
    if (access === '0') {
        cssThemeTag.href = cssThemeTag.href.replace("-access.css", ".css");
    } else {
        cssThemeTag.href = cssThemeTag.href.replace(".css", "-access.css");
    }
}

function readDisplaySettings() {
    let dark;
    let access;
    if (localStorage.getItem('darkmode')) {
        dark = localStorage.getItem('darkmode');
    } else {
        localStorage.setItem('darkmode', '0');
        dark = '0';
    }
    if (localStorage.getItem('access')) {
        access = localStorage.getItem('access');
    } else {
        localStorage.setItem('access', '0');
        access = '0';
    }
    return {
        'darkmode' : dark,
        'access' : access
    }
}

let themeset = readDisplaySettings();
setCSSColourDarkMode(themeset['darkmode']);
setCSSAccessMode(themeset['access'])
