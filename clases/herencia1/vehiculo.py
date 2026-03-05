
class Vehiculo(object):
    def __init__(self, matricula, modelo, potenciaCV):
        self.matricula = matricula
        self.modelo = modelo
        self.potenciaCV = potenciaCV
    
    def __str__(self):
        return self.matricula + " " + self.modelo + " " + str(self.potenciaCV)

    def encender(self):
        print("encendido vehículo")
        
    def acelerar(self):
        print("acelerando vehículo")
        
    def frenar(self):
        print("frenando vehículo")