from flask_restful import Resource 
from flask_mysqldb import MySQL
from flask import current_app

class CategoriaApi(Resource):
    def get(self):
        mysql= MySQL(app)
        cur= mysql.connection.cursor()
        return "categoria"