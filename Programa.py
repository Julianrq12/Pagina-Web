from flask import Flask, render_template
from db import db
from Estudiante import Estudiante


class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3"
        
        # Agregar la db a la app
        db.init_app(self.app)
        
        self.app.add_url_rule('/nuevo', view_func=self.agregar)
        
        #Iniciar Servidor
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)
    
    def agregar(self):
        return render_template('nuevoEstudiante.html')
    
    
    
miPrograma=Programa()