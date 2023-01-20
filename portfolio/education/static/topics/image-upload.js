// Function to insert text into a textfield at the current location
// This code was adapted from Stack Overflow post by GMKHussain 2021-01-19
// accessed on 2023-01-12
// https://stackoverflow.com/a/65793635
function addContentAtCursorFunc( elem, newContent ) {
    if (elem.selectionStart || elem.selectionStart == '0') {
        let _startSelection = elem.selectionStart;
        let _endSelection = elem.selectionEnd;
        elem.value = elem.value.substring(0, _startSelection)
            + newContent
            + elem.value.substring(_endSelection, elem.value.length);
    } else {
        elem.value += newContent;
    }
}
// end of referenced code

let imagePreview = document.getElementsByClassName('image-preview')[0];
let IMGText = document.getElementById('img-text');
let content = document.getElementById('content');

let btnUpload = document.getElementById('upload');

btnUpload.addEventListener('click', () => {
    let file = document.getElementById('imageupload');
    let data = new FormData();
    data.append("image", file.files[0]);

    fetch("image-upload", {
        method: 'POST',
        body: data
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        let messageDIV = document.getElementById('upload-message-div');
        let messageP = document.getElementById('upload-message-p');
        if (data.status) {
            let newli = document.createElement('li');
            let newimg = document.createElement('img');
            newimg.src = data.path;
            newimg.classList.add("uploadedimage");
            newimg.id = `img-${data.name}`;
            newimg.addEventListener('click', () =>{
                let md = `![Please type alt information here](${data.path})`;
                addContentAtCursorFunc(content, md);
            });
            newli.append(newimg);
            imagePreview.append(newli);
            imagePreview.classList.remove('hidden');
            IMGText.innerText = "Click on an image to insert the markdown code at the current selected location.";
            messageDIV.classList.add('info');
            messageDIV.classList.remove('error');
            messageDIV.classList.remove('hidden');
            file.value = null;
        } else {
            messageDIV.classList.add('error');
            messageDIV.classList.remove('info');
            messageDIV.classList.remove('hidden');
        }
        messageP.innerHTML = data.message;
    });
})

// Adding event listeners for pictures already uploaded
for (let li of imagePreview.children) {
    let image = li.children[0];
    image.addEventListener('click', () => {
        let md = `![Please type alt information here](${image.attributes.src.value})`;
        addContentAtCursorFunc(content, md);
    });
}