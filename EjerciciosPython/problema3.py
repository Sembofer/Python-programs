
# a) Función recursiva obtiene el maximo valor de una lista de naturales.

def Maximo(list,index):
    if list!=[] and index!=len(list):
        if list[index]>list[0]:
            list=list[index:]
            if len(list)==1:
                print(list[0])
            else:
                Maximo(list,1)
        else:
            Maximo(list,index+1)
    else:
        print( list[0])

##########################################################################################################

# b) Función recursiva que recibe como parámetro una lista de naturales 
# y muestra todos los números de dicha lista desde el último al primero.

def inve(L,j):
    if len(L)-j>=0:
        print(L[len(L)-j])
        inve(L,j+1)
    else: 
        print('fin')

##########################################################################################################

# c)  p(x) = a_n x^n + ...+ a_1 x + a_0 x^0 se representa mediante a_n, a_{n-1}, ..., a_1, a_0. 
# Función recursiva que evalúe un polinomio usando la regla de Honer:
# p(x)= ((..((a_n * x )  +  a_{n-1} )x + ... + a_1)x + a_0 )

def pol(x,L,n,j):
    if n>j:
        return ((pol(x,L,n,j+1))*x + L[n-j])
    else:
        return L[0]

##########################################################################################################

######################################### RELLENAR UNA LISTA L #############################################
n=int(input("Ingresa la longitud de la lista:"))
L=[]
print("Ingrese los valores de la lista L:")                         
for i in range(0,n):                                                
    L.append(int(input()))                                          
print("Según los números ingresados, la lista L es:", L) 
#############################################################################################################

######################################## Prueba del inciso a) ############################################
print("El valor maximo de la lista L es:")      ##########################################################
Maximo(L,1)                                     ################# Llamar a la función max ################
##########################################################################################################

######################################## Prueba del inciso b) ##############################################
print("Números de una lista desde el último al primero:")
inve(L,1)                                                   ###### Llamar a la función max #################
############################################################################################################

####################################### Prueba inciso c) ##################################################
print('Si la lista L representa una función polinomial. La evaluación de P(x) es la siguiente:')
x=int(input('Ingrese el valor de la variable x para evaluar el polinomio:'))

print(pol(x,L,len(L)-1,0))
###########################################################################################################