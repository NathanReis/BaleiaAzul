

window.onload = () => {
    const url = baseUrl + '/containers';
    let cardsContainer = document.getElementById('cards');

    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            let containers = data.data;

            for (let index = 0; index < containers.length; index++) {
                const container = containers[index];

                let card =
                    ` 
                    <li class="cards_item" id="${container.id}">
                        <div class="card">
                            <div class="card_image"><img width="300" height="200" src="../assets/docker.png"></div>
                            <div class="card_content">
                                <h2 class="card_title">${container.name}</h2>
                                <p class="card_text">Status: ${container.status}</p>
                                <p class="card_text">Imagem: ${container.image.tags[0]}</p>
                                <div class="d-flex">
                                    <span class="btn card_btn" onclick="startContainer('${container.id}')">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
                                            class="bi bi-play" viewBox="0 0 16 16">
                                            <path
                                                d="M10.804 8 5 4.633v6.734L10.804 8zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696l6.363 3.692z" />
                                        </svg>
                                        <p>Iniciar</p>
                                    </span>
                                    <span class="btn card_btn" onclick="stopContainer('${container.id}')">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
                                            class="bi bi-stop-fill" viewBox="0 0 16 16">
                                            <path
                                                d="M5 3.5h6A1.5 1.5 0 0 1 12.5 5v6a1.5 1.5 0 0 1-1.5 1.5H5A1.5 1.5 0 0 1 3.5 11V5A1.5 1.5 0 0 1 5 3.5z" />
                                        </svg>
                                        <p>Parar</p>
                                    </span>
        
                                </div>
                                <div class="d-flex">
                                    <span class="btn card_btn">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor"
                                            class="bi bi-eye" viewBox="0 0 16 16">
                                            <path
                                                d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z" />
                                            <path
                                                d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z" />
                                        </svg>
                                        <p>Visualizar</p>
                                    </span>
                                    <span class="btn card_btn" onclick="deleteContainer('${container.id}')">
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

function deleteContainer(id) {
    const url = baseUrl + '/containers/';
    fetch(url + id, {
        method: 'DELETE',
    })
        .then(res => res.text()) // or res.json()
        .then(res => {
            console.log(res)
            document.location.reload(true);
        })
}

function addContainer() {
    const url = baseUrl + '/containers/run';

    let portC = String(document.getElementById('defaultForm-portC').value)
    let portH = Number(document.getElementById('defaultForm-portH').value)
    let port = { [portC]: portH }


    let container = {
        'image': document.getElementById('defaultForm-image').value,
        'port': port
    }

    let fetchData = {
        method: 'POST',
        body: JSON.stringify(container),
        headers: { 'Content-Type': 'application/json' }
    }

    fetch(url, fetchData)
        .then(function (res) {
            console.log(res);
            document.location.reload(true);
        });
}


function startContainer(id) {
    const url = baseUrl + '/containers/start/' + id;

    let fetchData = {
        method: 'POST',
    }

    fetch(url, fetchData)
        .then(function (res) {
            console.log(res);
            document.location.reload(true);
        });

}


function stopContainer(id) {
    const url = baseUrl + '/containers/stop/' + id;

    let fetchData = {
        method: 'POST',
    }

    fetch(url, fetchData)
        .then(function (res) {
            console.log(res);
            document.location.reload(true);
        });

}