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
