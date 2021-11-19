
window.onload = () => {
    const url = baseUrl + '/images';
    let cardsContainer = document.getElementById('cards');

    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            let images = data.data;

            for (let index = 0; index < images.length; index++) {
                const image = images[index];

                let card =
                    ` 
                          <li class="cards_item" id="${image.id}">
                                <div class="card">
                                    <div class="card_image"><img width="300" height="200" src="../assets/docker.png"></div>
                                    <div class="card_content">
                                        <h2 class="card_title">${image.tags[0].split(':')[0]}</h2>
                                        <p class="card_text">${image.tags[0].split(':')[1]}</p>
                                        <div class="d-flex">
                                           
                                            <span onclick="deleteImage('${image.id}')" class="btn card_btn">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
                                                    class="bi bi-trash" viewBox="0 0 16 16">
                                                    <path
                                                        d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z" />
                                                    <path fill-rule="evenodd"
                                                        d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z" />
                                                </svg>
                                                <p>Deletar</p>
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </li>
                    `
                cardsContainer.innerHTML += card;
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

function deleteImage(id) {
    const url = baseUrl + '/images/';
    fetch(url + id, {
        method: 'DELETE',
    })
        .then(res => res.text()) // or res.json()
        .then(res => {
            console.log(res)
            document.location.reload(true);
        })
}

function deleteAllImages() {
    const url = baseUrl + '/images';
    fetch(url, {
        method: 'DELETE',
    })
        .then(res => res.text()) // or res.json()
        .then(res => {
            console.log(res)
            document.location.reload(true);
        })
}

function addImage() {
    const url = baseUrl + '/images';

    let image = {
        'name': document.getElementById('defaultForm-name').value,
        'tag': document.getElementById('defaultForm-tag').value
    }

    let fetchData = {
        method: 'POST',
        body: JSON.stringify(image),
        headers: { 'Content-Type': 'application/json' }
    }

    let spinner = document.getElementById('loading');
    let btn = document.getElementById('btn_add');
    btn.hidden = true;
    spinner.hidden = false;

    fetch(url, fetchData)
        .then(function (res) {
            console.log(res);
            btn.hidden = false;
            spinner.hidden = true;
            document.location.reload(true);
        });

}