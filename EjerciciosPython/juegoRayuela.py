# JUEGO DE LA RAYUELA 
# Escribir una función recursiva que calcule el número de caminos posibles
# para alcanzar un adoquín objetivo numerado con "n" mayor que cero.

######### Como punto de partida, hay dos caminos sencillos: 1) camino con saltos de uno en uno.
######### 2) camino saltando al inicio el número 1 y seguido de saltos de uno en uno.

# A partir del tercer camino, cuando se salta el adoquín 2, el número de caminos posibles corresponde al
# número de caminos posibles para llegar a n más el número de caminos posibles para llegar a (n-1), así sucesivamente.
# Se muestra la sumatoria \sum_{i=1}^n i , donde n es el límite superior o el número de adoquín objetivo. #
#################### Aquí la sumatoria se hace en retroceso. Por ejemplo 5+4+3+2+1. ##########################
def sumatoria(n):
    if n==1:
        return 1
    else: 
        return n + sumatoria(n-1)
##############################################################################################################
##############################################################################################################
n=int(input("Ingresa el número de adoquín objetivo:"))  ################ Adoquín objetivo. ###################
z= sumatoria(n) + 2                        ### Resultado de la sumatoria más los dos primeros casos sencillos. 
print("Resultado", z)                      ############## Muestra el resultado final. #######################
##############################################################################################################