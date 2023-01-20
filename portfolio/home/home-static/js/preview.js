let btnPreview = document.getElementById('preview');

btnPreview.addEventListener('click', function(){
    let title = document.getElementById('title').value;
    let markdown = document.getElementById('content').value;
    let previewDiv = document.getElementById('preview-area');

    fetch("preview", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'title': title,
            'markdown': markdown
        })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(html) {
        previewDiv.innerHTML = `<div class="content">${html.html} </div>`;
        previewDiv.scrollIntoView({behavior: "smooth"});
    });
})
