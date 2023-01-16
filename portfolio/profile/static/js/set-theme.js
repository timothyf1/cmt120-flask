function setCSSColourDarkMode(darkmode, access) {
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

function setDarkMode(value) {
    localStorage.setItem('darkmode', value);
    setCSSColourDarkMode(`${value}`);
}

function setAccessMode() {
    let accessCheckBox = document.getElementById("accessibility")
    if (accessCheckBox.checked) {
        localStorage.setItem('access', '1');
        setCSSAccessMode('1')
    } else {
        localStorage.setItem('access', '0')
        setCSSAccessMode('0')
    }
    // setCSSColourDarkMode(`${value}`);
}

function setCurrentSettings() {
    let currentSetting = readDisplaySettings();
    let currentRadio = document.getElementById(`dark-${currentSetting['darkmode']}`);
    currentRadio.checked = true;
    let accessCheckBox = document.getElementById("accessibility");
    if (currentSetting['access'] === '0') {
        accessCheckBox.checked = false;
    } else {
        accessCheckBox.checked = true;
    }
}

setCurrentSettings();
