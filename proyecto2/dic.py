######### archivo para facilitar el tratamiento de las palabras en el main ##########

#variable para las instrucciones
"""instrucciones = "INSTRUCCIONES: el juego consiste en adivinar la palabra según la cantidad de letras\ncon LA BARRA ESPACIADORA puedes reiniciar el juego y saldras del juego con ESC\nAmarillo: significa que la letra esta en la palabra pero no en la posicion correcta\nVerde: significa que la letra está en la poscicion correcta\nGris: significa que no esta en la palabra\npreciona BARRA ESPACIADORA para continuar"""
instrucciones = "ingrese la dificultad (entre 4:muy facil y 8:muy dificil) :"


#dicionarios para asegurar un O(1) en procesos
palabras_4 = {}
palabras_5 = {}
palabras_6 = {}
palabras_7 = {}
palabras_8 = {}



#procesos para separar las palabras en sus respectivos diccionarios
con = 0
archivo = open("palabras.txt")
for i in archivo:
    if len(i.replace("\n","")) == 4:
        palabras_4[con] = (i.replace("\n",""))
        con += 1
archivo.close()

archivo = open("palabras.txt")
con = 0
for i in archivo:
    if len(i.replace("\n","")) == 5:
        palabras_5[con] = (i.replace("\n",""))
        con += 1
archivo.close()

archivo = open("palabras.txt")
con = 0
for i in archivo:
    if len(i.replace("\n","")) == 6:
        palabras_6[con] = (i.replace("\n",""))
        con += 1
archivo.close()

archivo = open("palabras.txt")
con = 0
for i in archivo:
    if len(i.replace("\n","")) == 7:
        palabras_7[con] = (i.replace("\n",""))
        con += 1
archivo.close()

archivo = open("palabras.txt")
con = 0
for i in archivo:
    if len(i.replace("\n","")) == 8:
        palabras_8[con] = (i.replace("\n",""))
        con += 1
archivo.close()

