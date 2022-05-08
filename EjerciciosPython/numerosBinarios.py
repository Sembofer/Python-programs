# Procedimiento recursivo incremento que le suma 1 a un número binaro, sin duplicar la lista

def Bin(L,j):
    A=[0]
    if (len(L)-j) !=0:
        if L[len(L)-1]==0:
            if L[len(L) - j]==0:
                Bin(L,j+1)            
            else:
                #print(len(L)-j)
                L[len(L)-1]=1
                print(L)
        else:
            if L[len(L) - j]==1:
                Bin(L,j+1)
            else:
                #print(len(L)-j)
                L[len(L)-j]=1
                for i in range(len(L)-j+1,len(L)):
                    L[i]=0
                print(L)
    elif (len(L)-j)==0 and L[0]==0:
        L[len(L)-1]=1
        print(L)
    elif (len(L)-j)==0 and L[0]==1:
        L[0]=1
        for k in range(1,len(L)):
            L[k]=0
        print(L+A)


######################## Rellenar la lista que represena el número binario ################################
###########################################################################################################
n=int(input('Longitud del número binario:'))
L=[]
print('Ingrese los valores del número binario (recordar que los valores permitidos son 0 y 1):')
for l in range(0,n):
    L.append(int(input()))
print('El número binario es:',L)
########################################################################################################

######################################### Prueba de la función #########################################
print('El resultado de sumarle 1 al número binario es:')
Bin(L,1)
#########################################################################################################