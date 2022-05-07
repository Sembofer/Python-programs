# Procedimiento recursivo que devuelve el elemento mayor de una lista




def max(list,index):                        # La lista es L definida abajo y el índice comienza con 1.
    if list!=[] and index!=len(list):   
        if list[index]>list[0]:             # Compara los elementos de L, si el indexado es mayor que el primero,
            list=list[index:]               # corta la lista a partir del indexado, el mayor.
            if len(list)!=1:                # Si el corte no ha llegado hasta el último elemento, entonces
                max(list,1)                 # entra en recursión para seguir comparando con los siguientes elementos.
            else:                           # Cuando el corte llega al último, 
                print(list[0])              # Este lo muestra como el máximo.
        else:                               # Si el elemento indexado no es mayor al primero (o primero luego del corte),
            max(list,index+1)               # entonces pasa a comparar si el siguiente elemento es mayor mediante recursión.
    else:
        print( list[0])                     # Muestra el mayor cuando el máximo se encuentra en algun lugar de la lista que no sea el último.



######################################### RELLENAR LA LISTA ##############################################
longList=int(input("Ingresa la longitud de la lista:")) # Tamaño de la lista
List=[]                                             # Lista L vacías L[None]
print("Ingrese los valores de la lista L:")      # Pide rellenar L                  
for i in range(0,longList):                             # mediante el bucle for.
    List.append(int(input()))                       
print("Según los números ingresados, la lista L es:", List) # Muestra la lista L
###########################################################################################################


print("El valor maximo de la lista L es:")      
max(List,1)                                        # Llamar a la función max

