from flask import Flask
app = Flask(__name__)

in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}


@app.get('/prog_lg')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}

@app.route('/prog_lg/<programming_language_name>')
def get_programming_language(programming_language_name):
   return in_memory_datastore[programming_language_name]
@app.get("/prog_lg/test")
def test_hi():
   return {"I'm working"}