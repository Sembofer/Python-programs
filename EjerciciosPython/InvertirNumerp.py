# Programa para invertir un número (Solo enteros)
# Ej. 123 -> 321

def residuo(invNum):                  
    numDigitos=len(str(invNum))				# Cantidad de dígitos que componen el número a.     Ej = 3
    Orden= 10**(numDigitos-1) 				# Orden para recolocar los dígitos.     Ej = 100
    if invNum!=0:
        ultDig= (invNum%10)       			# Ultimo dídito del número a.   Ej = 3
        Coloca=ultDig*Orden       			# Coloca el dígito de acuerdo con Ord.      Ej = 300
        invNum= invNum//10            		# Toma la parte entera de la división.      Ej = 12, es decir, ahora a=12
        return Coloca + residuo(invNum)    	# Guarda la suma ordenada.  Ej = 300 + 20 + 1
    else:
        return 0            				# Si a=0 suma cero, osea que solo toma en cuenta el return del if.




num=int(input("Ingresa el número a invertir:"))      # Pide el número al usuario y lo convierte en entero
print("Resultado", residuo(num))                     