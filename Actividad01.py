class Cliente:
    def __init__(self):
        self.nombrep = input("Nombre del dueño de la vivienda? ")
        self.rut = input("Rut del dueño de la vivienda? ")

class Medidor:
    def __init(self, electro):
        self.electro = int(electro)
    def mostrar(self):
        return self.electro

    
class Departamento(Cliente, Medidor):
    def __init__(self):
        self.número = input("número del departamento? ")
        
    
class Edificio(Departamento):
    def __init__(self):
        self.dirección2 = input("Cual es la dirección del edificio? ")
        self.nombre = input("Cual es el nombre del edificio? ")
        self.departamentos = []
        while True:
            self.electro = int(input("Cuanto marca el medidor común? "))
            if self.electro<0:
                print("Valor de medidor no válido")
            else:
                break
        self.es_electro = False
        if self.electro<10000:
            self.es_electro = True
        self.departamentos = []
        self.edificios.append([self.dirección2,self.nombre,self.es_electro])
        Departamento.__init__(self)
        
class Casa(Cliente, Medidor):
    def __init__(self):
        self.dirección = input("Cual es la dirección de la casa? ")
        while True:
            self.electro = int(input("Cuanto marca el medidor? "))
            if self.electro<0:
                print("Valor de medidor no válido")
            else:
                break
        self.es_electro = False
        if self.electro<5000:
            self.es_electro = True
        Cliente.__init__(self)
        self.casas.append([self.dirección,self.es_electro,self.nombrep,self.rut ])


class Comuna(Casa, Edificio):
    def __init__(self, nombre):
        self.nombre = nombre
        self.comunas.append(nombre)
        self.casas = []
        self.edificios = []
        while True:
            self.vivienda = input("Es una Casa o un Edificio? ")
            self.vivienda = self.vivienda.lower()
            if self.vivienda == "casa" or self.vivienda == "edificio":
                break
            else:
                print("Vivienda incorrecta")
        if self.vivienda == "casa":
            Casa.__init__(self)
        else:
            Edificio.__init__(self)


class Ciudad(Comuna):
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.comunas = []
    def llamar(self):
        Comuna.__init__(self, nombre = input("Nombre comuna: "))
        print(self.comunas)
        print(self.casas)
        print(self.edificios)
    def __str__(self):
        frase = "La ciudad escogida es "+ self.ciudad + "."
        return frase
    

a = Ciudad(input("Qué ciudad es? "))
print(a)
a.llamar()
a.llamar()     
