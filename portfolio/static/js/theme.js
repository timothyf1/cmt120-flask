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

function setCSSTheme(themeset) {
    let themetag = document.createElement('link')
    themetag.setAttribute('rel', 'stylesheet')
    themetag.setAttribute('type', 'text/css')
    themetag.setAttribute('id', 'theme')
    switch (themeset['darkmode']) {
        case '0':
            themetag.setAttribute('href', themeset['access'] === '0' ? '/static/css/system.css' : '/static/css/system-access.css')
            break;
        case '1':
            themetag.setAttribute('href', themeset['access'] === '0' ? '/static/css/light.css' : '/static/css/light-access.css')
            break;
        case '2':
            themetag.setAttribute('href', themeset['access'] === '0' ? '/static/css/dark.css' : '/static/css/dark-access.css')
            break;
    }

    document.getElementsByTagName('head')[0].appendChild(themetag)

    if (themeset['access'] === '1') {
        let accesstag = document.createElement('link')
        accesstag.setAttribute('rel', 'stylesheet')
        accesstag.setAttribute('type', 'text/css')
        accesstag.setAttribute('href', '/static/css/access.css')
        document.getElementsByTagName('head')[0].appendChild(accesstag)
    }
}

let themeset = readDisplaySettings();
setCSSTheme(themeset)
