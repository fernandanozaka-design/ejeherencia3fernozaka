from clases.herencia1.taxi import Taxi
from clases.herencia1.auto_particular import AutoParticular


def main():
    coche = Taxi("123-GTO","Versa",1000, "123-a")
    print("***************************")
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()
    #crear objeto de la clase
    # def __init__(self, clave, nombre, edad, marca, color, placa)
    ap= AutoParticular("123","mony",15,"volvo","plata","987-G")#pasar los valores como parámetro
    #imprimir objeto
    print(ap)
    #llamar métodos funcionales
    ap.subirseAuto() 
    ap.arrancarAuto()
    ap.llegarDestino()
    ap.bajandoAuto()
    
    
    
    
if __name__ == "__main__":
    main()
    