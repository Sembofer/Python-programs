# Problema de la torre de Hanoi




def hanoi(n,tInicio,tApoyo,tDestino):
    """_summary_

    Argumentoss:
        n (entero): número de discos
        tInicio : Torre de partida que contiene todos los n discos.
        tApoyo :  Torre destino que recibe todos los n discos.
        tDestino :  Torre por donde fluyen los discos para llegar a la torre destino.
    """
    if (n==1):
        print('Mueve el disco de la torre '+str(tInicio)+' a la torre '+str(tDestino))
    else:
        hanoi(n-1, tInicio,tDestino, tApoyo)
        print('Mueve el disco de la torre '+str(tInicio)+' a la torre '+str(tDestino))
        hanoi(n-1, tApoyo,tInicio, tDestino)

d = int(input('Numero de discos: '))
hanoi(d,'A', 'B', 'C')
