from flask import Flask, render_template


class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3"
        
        self.app.add_url_rule('/nuevo', view_func=self.agregar)
        
        #Iniciar Servidor
        self.app.run(debug=True)
    
    def agregar(self):
        return render_template('nuevoEstudiante.html')
    
    
    
miPrograma=Programa()