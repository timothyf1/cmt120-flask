function setDarkMode(value) {
    localStorage.setItem('darkmode', value);
    setCSSColourFile(`${value}`);
}

function setCurrentDarkModeRadio() {
    let currentSetting = readDarkModeSetting();
    let currentRadio = document.getElementById(`dark-${currentSetting}`);
    currentRadio.checked = true;
}

setCurrentDarkModeRadio();
