class cliente:
    def __init__(self, nombrep,rut):
        self.nombrep = nombrep
        self.rut = rut

        
class departamento(cliente):
    def __init__(self, medidor, número, electro):
        self.medidor = medidor
        self.número = número
        self.electro = electro

    
class edificio(departamento):
    def __init__(self, dirección, nombre, medidor, num_depto):
        self.dirección = dirección
        self.nombre = nombre
        self.medidor = medidor
        self.num_depto = num_depto
        

class casa(cliente):
    def __init__(self, medidor, dirección, electro):
        self.medidor = medidor
        self.dirección = dirección
        self.electro = electro
        

class comuna(casa, edificio):
    viviendas=[]
    


class ciudad(comuna):
    Santiago=[]
    

# Ciudad: Santiago
# Comunas: Las Condes y Vitacura

while True:
    while True:
        vivienda=input("Casa, Departamento o Edificio? ")
        if vivienda == "Casa" or vivienda == "Departamento" or vivienda == "Edificio":
            break
        else:
            print("Tipo de vivienda no válido")
    while True:
        Comuna=input("Las Condes o Vitacura? ")
        if Comuna == "Las Condes" or Comuna == "Vitacura":
            break
        else:
            print("Comuna no válida")
    while True:
        medidor=int(input("Medidor? "))
        if medidor>0:
            break
        else:
            print("Valor inválido de consumo.")

    
    
        
