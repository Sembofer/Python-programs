# Dada una lista de enteros positivos,
# se indica la mínima cantidad de elementos consecutivos al final de la lista
# cuya suma sea mayor o igual que una determinada cantidad C, que se recibe como parámetro.


def SumC(ElemenPosi,Elemen,Cantidad):
    if ElemenPosi>Cantidad or ElemenPosi==Cantidad:
        print('La mínima cantidad de elementos consecutivos al final de la lista es:', Elemen)
    else:
        SumC(ElemenPosi+Lista[len(Lista)-(Elemen+1)],Elemen+1,Cantidad)




############################# Rellenar la lista L #####################################################
Lista=[]
tamLista=int(input("Ingrese el tamaño de la lista:"))
print('A continuación rellena la lista')
for i in range(0,tamLista):
    Lista.append(int(input()))
print("La lista es:", Lista)
#######################################################################################################



# Validacion llamando a la funcion SumC
Cantidad=int(input("Establezca la cantidad de la suma:"))
SumC(Lista[len(Lista)-1],1,Cantidad)
#########################################################################################################