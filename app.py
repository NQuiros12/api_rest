from flask import Flask, make_response,jsonify
import json
from db import Connector
app = Flask(__name__)

""" in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}
 """
conn = Connector("bookstore","localhost","root","example")
conn.connect()
@app.get('/countries')
def countries():
   conn.execute("select * from pais limit 1;") ##### Modificar esta query
   rs = conn.fetchall()
   results_json = json.dumps([{"code": r[0], "capital": r[1]} for r in rs])
   return results_json  
@app.route('/countries/<countrie>')
def countrie(countrie):
   conn.execute(f"select * from pais where nombre = '{countrie}' limit 1;") ##### Modificar esta query
   rs = conn.fetchone()
   #For some reason this is getting me a float.
   #results_json = json.dumps([{"code": r[0], "name": r[1]} for r in rs])
   return jsonify(rs)
@app.get("/countries/test")
def test_hi():
   response = make_response('the API works!', 200)
   response.mimetype = 'text/plain'
   return response