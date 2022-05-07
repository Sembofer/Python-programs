# Programa que, dado un arreglo constituido de números enteros, 
# utiliza una función que devuelve la suma de todos los números 
# mayores al último elemento del arreglo. 


def suma(arreglo,ultimoNumero):
    if arreglo!=[]:                                                 # Se ocupa porque el arreglo se va cortando.
        if arreglo[0] >ultimoNumero:                                # Compara, si el primer elemento es mayor que el último, entonces
            return arreglo[0] + suma(arreglo[1:],ultimoNumero)      # guarda tal número y corta a partir del siguiente para sumar. Entra en recursión
        else:
            return suma(arreglo[1:],ultimoNumero)                   # Si el primer elemento del arreglo no es mayor que el último lo exluye y pasa al siguiente.
    else:                                                           # El último corte, cuando el arreglo ya no tiene elementos.
        return 0





longitudArreglo  = int(input('Ingresar la longitud del arreglo:'))          # Tamaño del arreglo.
lista   = []                                                                # El arreglo A[None], para rellenarlo.
print("Ingrese los valores del arreglo:")                                   # Rellenar A[].
for i in range(0,longitudArreglo):                                          # Para los índices A[A_0, A_1,...,A_n].
    lista.append(int(input()))                                              # Guarga los valores en A_j, ya convertidos en enteros.
print("Según los números ingresados, el arreglo es:", lista)                # Muestra el arreglo A con los datos ingresados.
ultiNum    = lista.pop()                                                    # Último elemento de A, o sea, A_n.



print('La suma de todos los números que son mayores al último del arreglo son:', suma(lista,ultiNum))                                           # Llama la función
