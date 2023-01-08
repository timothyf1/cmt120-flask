function setDarkMode(value) {
    localStorage.setItem('darkmode', value);
    console.log(localStorage.getItem('darkmode'))
    setCSSColourFile(`${value}`)
}

function setCurrentDarkModeRadio() {
    let currentSetting = readDarkModeSetting()
    let currentRadio = document.getElementById(`dark-${currentSetting}`)
    currentRadio.checked = true
}

setCurrentDarkModeRadio()
