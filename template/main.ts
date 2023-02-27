class Book{
    id:number;
    title:string;
    height:number;
    publisher:string;
    author_id:number;
    author:string;
}
async function getBooksJSON(){
	let urlServer = 'http://localhost:8000/books';
    //Look for books by genre
    const txtSearch = document.getElementById("genreBox") as HTMLInputElement;
    if(txtSearch.value && txtSearch.value != ""){
        urlServer = 'http://localhost:8000/books_genre/' + txtSearch.value;
    }
    //API request
	let response = await fetch(urlServer, {
		method: 'GET',
        headers: {
			'Content-type': 'application/json',
			'Access-Control-Allow-Origin':'*'
		},
        mode: 'cors'
	});
	console.log(response);
    let books:Book[] = await response.json();
    let grillaHTML = "";
    grillaHTML = getHeader(grillaHTML);
    for (const book of books){
        grillaHTML += '<div class="row">';
        grillaHTML += '<div class="col">' + book.id + '</div>';
        grillaHTML += '<div class="col">' + book.title + '</div>';
        grillaHTML += '<div class="col">' + book.height .toString() + '</div>';
        grillaHTML += '<div class="col">' + book.publisher+ '</div>';
        grillaHTML += '<div class="col">' + book.author_id + '</div>';
        //grillaHTML += '<div class="col" onclick="editarArticulo('+art.id+')" style="cursor:pointer; color:green">Editar</div>';
        //grillaHTML += '<div class="col" onclick="eliminarArticulo('+art.id+')" style="cursor:pointer; color:red">Eliminar</div>';
        grillaHTML += '</div>';
    };
    var divArt = document.getElementById("listaArticulos");
    if(divArt)  {
        divArt.innerHTML  = grillaHTML;
    }
}
function getHeader(grillaHTML:string){
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
