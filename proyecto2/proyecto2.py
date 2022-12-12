#librerias 
import dic
import random
import pygame

#constantes para el codigo

puntaje = 0 #texto para mostrar el puntaje
dificultad = 0
margen = 10
gris = (70,70,80)
verde = (6,214,160)
amarillo = (255,209,102)

entrada = ""
adivinado = []
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
noAdivinado = alfabeto
GameOver = False

pygame.init()
pygame.font.init()
pygame.display.set_caption("Wordle")

tamano_cuadrado = (600-4*10-2*100)//5
Font = pygame.font.SysFont("free sans bold",tamano_cuadrado)
Font_pequeño = pygame.font.SysFont("free sans bold",tamano_cuadrado//3)
texto_puntos = pygame.font.SysFont("free sans bold",30,True)

###########################funciones ############################

#funcion para escoger la palabra ganadora
def ganador_dic(dificultad):
    if dificultad == 4:
        return random.choice(dic.palabras_4)
    elif dificultad == 5:
        return random.choice(dic.palabras_5)
    elif dificultad == 6:
        return random.choice(dic.palabras_6)
    elif dificultad == 7:
        return random.choice(dic.palabras_7)
    elif dificultad == 8:
        return random.choice(dic.palabras_8)

#funcion para dar más intentos
def det_noAdivinadas(intento):
    letras_adivinadas = "".join(intento)
    letras_No_adivinadas = ""
    for letra in alfabeto:
        if letra not in letras_adivinadas:
            letras_No_adivinadas += letra
    return letras_No_adivinadas

#funcion para dar color a las letras
def det_color(intento, j):
    letra = intento[j]
    if letra == ganador[j]:
        return verde
    elif letra in ganador:
        return amarillo

        ########### para que detecte los numero repetidos ################# NOTA: no funciona bien
        """n_objetivo = ganador.count(letra)
        n_correcto = 0
        n_ocurrence = 0
        for i in 5:
            if intento[i] == letra:
                if i <= j:
                    n_ocurrence +=1
                if letra == ganador[j]:
                    n_correcto += 1
        if n_objetivo - n_correcto - n_ocurrence >= 0:
            return amarillo"""

    return gris

########################### ventana de presentacion del juego  y seleccion de dificultad ##################
entrada_presentacion = ""


ventana_presentacion = pygame.display.set_mode((600,700))
animacion_presentacion = True
while animacion_presentacion:
    ventana_presentacion.fill("white")


    letras_presentacion = Font_pequeño.render(dic.instrucciones, False, gris)
    enter = Font_pequeño.render("",False,gris)
    surface = letras_presentacion.get_rect()
    ventana_presentacion.blit(letras_presentacion,surface)
    ventana_presentacion.blit(enter,surface)

    #-cuadrado = pygame.Rect(200,200,tamano_cuadrado,tamano_cuadrado)
    #pygame.draw.rect(ventana_presentacion, gris, cuadrado, width=2,border_radius=3)

    letra_presentacion = Font.render(entrada_presentacion, False, gris)
    surface_presentacion = letra_presentacion.get_rect(center = (200+tamano_cuadrado//2, 200+tamano_cuadrado//2))
    ventana_presentacion.blit(letra_presentacion,surface)

    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            animacion_presentacion = False
        if evento.type == pygame.KEYDOWN:
        #para cerar la ventana
            if evento.key == pygame.K_ESCAPE:
                animacion_presentacion = False
            if evento.key == pygame.K_4:
                dificultad = 4
            if evento.key == pygame.K_5:
                dificultad = 5
            if evento.key == pygame.K_6:
                dificultad = 6
            if evento.key == pygame.K_7:
                dificultad = 7
            if evento.key == pygame.K_8:
                dificultad = 8
            if evento.key == pygame.K_BACKSPACE:
                    if len(entrada)  > 0:
                        entrada = entrada[:len(entrada)-1]

            if len(entrada_presentacion) < 1:
                entrada_presentacion = entrada + evento.unicode
                print(entrada)
                
            
    pygame.display.flip()
print(dificultad)

#Creacion de la plabra para ganar
ganador = ganador_dic(dificultad)

#creacion de la ventana del juego
ventana = pygame.display.set_mode((900,700))

print(ganador)

#animacion en loop
animacion = True
while animacion:
    #fondo
    ventana.fill("white")

    #dibujamos las letras en la ventana
    letras = Font_pequeño.render(noAdivinado,False,gris)
    surface = letras.get_rect(center = (600//2,100//2))
    ventana.blit(letras,surface)

    puntos = texto_puntos.render("Puntaje: "+str(puntaje),1,(0,0,0))
    ventana.blit(puntos,(350,10))

    #dibujamos los cuadrados para la palabra
    y = 100
    for i in range(6):
        x = 100
        for j in range(len(ganador)):

            #cuadrado
            cuadrado = pygame.Rect(x,y,tamano_cuadrado,tamano_cuadrado)
            pygame.draw.rect(ventana, gris, cuadrado, width=2,border_radius=3)

            #letras/palabras que ya se han adivinado
            if i < len(adivinado):
                color = det_color(adivinado[i], j)
                pygame.draw.rect(ventana, color, cuadrado,border_radius=3)
                letra = Font.render(adivinado[i][j], False, (255,255,255))
                surface = letra.get_rect(center = (x +tamano_cuadrado//2,y+tamano_cuadrado//2))
                ventana.blit(letra,surface)

            #entrada del usuario
            if i == len(adivinado) and j < len(entrada):
                letra = Font.render(entrada[j], False,gris)
                surface = letra.get_rect(center = (x +tamano_cuadrado//2,y+tamano_cuadrado//2))
                ventana.blit(letra,surface)

            x += tamano_cuadrado + margen
        y += tamano_cuadrado + margen

    #mostrar la respuesta correcta despues del GameOver
    if len(adivinado) == 6 and adivinado[5] != ganador:
        GameOver = True
        letra = Font.render(ganador, False, gris)
        surface = letras.get_rect(center = (300, 600))
        ventana.blit(letras, surface)

    #actualizacion de la ventana
    pygame.display.flip()

    #captar la interaccion del usuario
    for even in pygame.event.get():

        #para cerar la ventana
        if even.type == pygame.QUIT:
            animacion = False

        #captamos el teclado del usuario
        elif even.type == pygame.KEYDOWN:

            if even.key == pygame.K_ESCAPE:
                animacion = False

            #correcion del input
            if even.key == pygame.K_BACKSPACE:
                if len(entrada) > 0:
                    entrada = entrada[:len(entrada)-1]


            #para mostrar en pantalla
            elif even.key == pygame.K_RETURN:
                if len(entrada) == len(ganador) and  entrada:
                    adivinado.append(entrada)
                    noAdivinado = det_noAdivinadas(adivinado)
                    GameOver = True if entrada == ganador else False
                    if entrada == ganador:
                        puntaje += 1
                    entrada = ""


            #barra espaciadora para reiniciar 
            elif even.key == pygame.K_SPACE:
                GameOver = False
                ganador = ganador_dic(dificultad)
                print(ganador)
                adivinado = []
                noAdivinado = alfabeto
                entrada = ""


            #entrada de tecto
            elif len(entrada) < len(ganador) and not GameOver:
                entrada = entrada + even.unicode

