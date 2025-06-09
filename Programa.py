from flask import Flask


class Programa:
    
    def __init__(self):
        
        self.app=Flask(__name__)
        
        self.app.add_url_rule('/nuevo', view_func=self.agregar)
        
        #Iniciar Servidor
        self.app.run(debug=True)
    
    def agregar(self):
        return "Hola Mundo Flask"
    
    
    
miPrograma=Programa()