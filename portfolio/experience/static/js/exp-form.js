let current = document.getElementById('current');
let endDate = document.getElementById('end');

current.addEventListener('change', () => {
    if (current.checked) {
        endDate.setAttribute('disabled', '')
        endDate.value = ''
    } else {
        endDate.removeAttribute('disabled');
    }
});

if (current.checked) {
    endDate.setAttribute('disabled', '')
    endDate.value = ''
} else {
    endDate.removeAttribute('disabled');
}
