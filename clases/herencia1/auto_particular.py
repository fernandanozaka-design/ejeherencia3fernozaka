#referecia de la clase
from clases.herencia2.persona import Persona

class AutoParticular(Persona):
    def __init__(self, clave, nombre, edad, marca, color, placa):
        super().__init__(clave, nombre, edad)
        #inicializando las propiedades de la clase
        self.marca=marca
        self.color=color
        self.placa=placa
        
    #método STR
    def __str__(self):
        return super().__str__()+" "+ self.marca+" "+self.color+" "+self.placa
            
    #métodos funcionales
    def subirseAuto(self):
        print("subiendo al auto")
        
    def arrancarAuto(self):
        print("encendiendo el radio")
        print("arrancando el auto")
        
        
    def llegarDestino (self):
        print ("llegando al destimo")
        
        
    def bajandoAuto(self):
        print("bajando del auto")