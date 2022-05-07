# Función recursiva que permita calcular un término k de la siguiente serie 
# 1,2,3,6,11,20,37,...,m,n,o,(m+n+o),...


def termSerie(termino):
    if termino>0:
        if termino==1:
            return 1
        elif termino==2:
            return 2
        elif termino==3: 
            return 3
        else:
            return termSerie(termino-1) + termSerie(termino-2) + termSerie(termino-3)
    else:
        print("El término de la serie tiene que ser mayor que cero.")



term=int(input("Ingrese el término de la serie deseado:"))     # Pide el término al usuario
print(termSerie(term))                                         # Muestra el resultado
############################################################################################################