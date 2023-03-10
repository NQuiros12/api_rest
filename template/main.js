var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var Book = /** @class */ (function () {
    function Book() {
    }
    return Book;
}());
function getBooksJSON() {
    return __awaiter(this, void 0, void 0, function () {
        var urlServer, txtSearch, headers, requestInit, response, books, booksArray, _i, books_1, book, bookObj, grillaHTML, _a, booksArray_1, book, divArt;
        return __generator(this, function (_b) {
            switch (_b.label) {
                case 0:
                    urlServer = 'http://localhost:8000/books';
                    txtSearch = document.getElementById("genreBox");
                    if (txtSearch.value && txtSearch.value != "") {
                        urlServer = 'http://localhost:8000/books_genre/' + txtSearch.value;
                    }
                    headers = new Headers();
                    headers.append('Content-Type', 'application/json');
                    headers.append('Access-Control-Allow-Origin', '*');
                    requestInit = {
                        method: 'GET',
                        headers: headers,
                        mode: 'cors'
                    };
                    return [4 /*yield*/, fetch(urlServer, requestInit)];
                case 1:
                    response = _b.sent();
                    if (!(response.status === 200 || response.status === 304)) return [3 /*break*/, 3];
                    return [4 /*yield*/, response.json()];
                case 2:
                    books = _b.sent();
                    booksArray = [];
                    for (_i = 0, books_1 = books; _i < books_1.length; _i++) {
                        book = books_1[_i];
                        bookObj = {
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
                    grillaHTML = "";
                    grillaHTML = getHeader(grillaHTML);
                    grillaHTML += '<div class="table">';
                    for (_a = 0, booksArray_1 = booksArray; _a < booksArray_1.length; _a++) {
                        book = booksArray_1[_a];
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
                    }
                    ;
                    grillaHTML += '</div>';
                    divArt = document.getElementById("listBooks");
                    if (divArt) {
                        divArt.innerHTML = grillaHTML;
                    }
                    return [3 /*break*/, 4];
                case 3:
                    console.log("Error: " + response.statusText);
                    _b.label = 4;
                case 4: return [2 /*return*/];
            }
        });
    });
}
function getHeader(grillaHTML) {
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
