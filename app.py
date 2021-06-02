# from api.categoria_api import CategoriaApi
# from api.hello_api import HelloWorld
from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource,Api

app = Flask(__name__)
mysql= MySQL(app)
api = Api(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mito1997+'
app.config['MYSQL_DB'] = 'myblog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route("/")
def index():
    cur= mysql.connection.cursor()
    return "osi"

class HelloWorld(Resource):
    def get(self):
        return "hello world"

class CategoriaApi(Resource):
    def get(self):
        cur= mysql.connection.cursor()
        cur.execute("SELECT * FROM categoria")
        result = cur.fetchall()
        return str(result)


api.add_resource(HelloWorld, '/hello')
api.add_resource(CategoriaApi, '/categoria')
