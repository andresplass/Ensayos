kilometro=float(input("Cuanto hay corrido ctm? :"))
hora=float(input("Que hora eh shishetuamre? :"))
minutos=float(input("Cuantos minutos? :"))


#42.195 kilometros

distanciaquefalta=float(42.195)-kilometro

horasrestantes=float(4)-hora

horasenminutos=int(horasrestantes)*60
minutosrestantes=(horasenminutos-minutos)/60

velocidadnecesaria=42.195/4
print(velocidadnecesaria)


velocidad=(distanciaquefalta/minutosrestantes)
print(velocidad)

if horasrestantes<=0:
    print("se termino el tiempooooooooo")

print("Faltan",distanciaquefalta,"para terminar, deberas aumentar tu velocidad a",velocidad,"km/h")
