# Dados dos arreglos de números enteros A y B de longitud n y m  respectivamente, 
# siendo n>=m, determinar si B está contenido en A.





def cont(A,B,indexb,indexa):                # Comienza con los índices iguales a cero.                 
    if indexb<len(B) and indexa<len(A):     # si las comparaciones de los elementos de A y B no se acaban, esto sigue.
        if B[indexb] == A[indexa]:          # Compara si primer elemento de B es igual a alguno de A, entonces
            cont(A,B,indexb+1,indexa+1)     # compara si el siguiente elemento de B es igual al siguiente de A
        else:
            cont(A,B,0,indexa+1)            # Busca un elemento de A que sea igual al primer elemento de B
    elif (indexa<len(A) and indexb==len(B)) or indexb==len(B): # Cuando ya no hay elementos de B por compara con elemetos
        print("CONTENIDO")                          # de A, entonces muentra el mensaje CONTENIDO
    elif indexa>=len(A) and indexb!=len(B):    # Si ya se han comaparado todos los elementos de A y aún
        print("NO CONTENIDO")                 # hay elementos de B. Entonces muestra el mensaje NO CONTENIDO



##################################################################################################
n=int(input("Ingresar el tamaño de A:"))   # El tamaño de A.
m=int(input("Ingrsar el tamaño de B:"))    # El tamaño de B.
A=[]                                          # A vacío.
B=[]                                          # B vacío.
if n>=m:                                      # Es la condición de que A contenga a B.
    print("Ingrese los valores del arreglo A:")                         
    for i in range(0,n):                                                
        A.append(int(input()))                                          
        print("Según los números ingresados, el arreglo A es:", A)          
###############  Rellenado de A y B.  ###########
    print("Ingrese los valores del arreglo B:")                         
    for i in range(0,m):                                                
        B.append(int(input()))                                          
    print("Según los números ingresados, el arreglo B es:", B)          
    cont(A,B,0,0)                          # Llama la función
else:
    print("Error, el tamaño de A debe ser mayor a la de B")
###################################################################################################
