class Book {
    id: number;
    title: string;
    height: number;
    publisher: string;
    author_id: number;
    author: string;
}

async function getBooksJSON() {
    let urlServer = 'http://localhost:8000/books';
    //Look for books by genre
    const txtSearch = document.getElementById("genreBox") as HTMLInputElement;
    if (txtSearch.value && txtSearch.value != "") {
        urlServer = 'http://localhost:8000/books_genre/' + txtSearch.value;
    }
    // API request
    let headers: Headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    let requestInit: RequestInit = {
        method: 'GET',
        headers: headers,
        mode: 'cors'
    };

    let response: Response = await fetch(urlServer, requestInit);
    if (response.status === 200 || response.status === 304) {
        let books: Book[] = await response.json();
        let booksArray = [];

        for (const book of books) {
            let bookObj = {
                id: book[0],
                title: book[1],
                genre: book[2],
                height: book[3],
                publisher: book[4],
                author_id: book[5]
            };
            booksArray.push(bookObj);
        }

        console.log(booksArray);
        let grillaHTML: string = "";
        grillaHTML = getHeader(grillaHTML);
        grillaHTML += '<div class="table">';
        for (const book of booksArray) {
            console.log(book.id, book.title, book.height, book.publisher, book.author_id);
            grillaHTML += '<div class="row">';
            grillaHTML += '<div class="col">' + book.id + '</div>';
            grillaHTML += '<div class="col">' + book.title + '</div>';
            grillaHTML += '<div class="col">' + book.height + '</div>';
            grillaHTML += '<div class="col">' + book.publisher + '</div>';
            grillaHTML += '<div class="col">' + book.author_id + '</div>';
            //grillaHTML += '<div class="col" onclick="editarArticulo('+art.id+')" style="cursor:pointer; color:green">Editar</div>';
            //grillaHTML += '<div class="col" onclick="eliminarArticulo('+art.id+')" style="cursor:pointer; color:red">Eliminar</div>';
            grillaHTML += '</div>';
        };
        grillaHTML += '</div>';
        var divArt = document.getElementById("listBooks");
        if (divArt) {
            divArt.innerHTML = grillaHTML;
        }
    } else {
        console.log("Error: " + response.statusText);
    }

}

function getHeader(grillaHTML: string) {
    grillaHTML += '<div class="row">';
    grillaHTML += '<div class="col"><b>ID</b></div>';
    grillaHTML += '<div class="col"><b>TITLE</b></div>';
    grillaHTML += '<div class="col"><b>GENRE</b></div>';
    grillaHTML += '<div class="col"><b>HEIGHT</b></div>';
    grillaHTML += '<div class="col"><b>PUBLISHER</b></div>';
    /* 
    grillaHTML += '<div class="col"></div>';
    grillaHTML += '<div class="col"></div>'; */
    grillaHTML += '</div>';
    return grillaHTML;
}
