# Problema de la torre de Hanoi
# en proceso





def mov(A,index1a,index2a,T, index):
    if len(A[0])%2==0 and len(A[0])!=0:
        print(f'Mover {A[0][len(A[0])-1]} a {T[0+2]}')
        A[2]=A[2]+ A[0][len(A[0])-1]
        print(A[2])
        A[0]=A[0][:len(A[0])-1]
        print(A[0])
        mov(A,index1a,index2a,T,index)
    elif len(A[0])%2!=0 and len(A[0])!=0:
        print(f'Mover {A[0][len(A[0])-1]} a {T[0+1]}')
        A[0]=A[0][:len(A[0])-1] 
        print(A[0])
        A[1]=A[1]+ A[0][len(A[0])-1]
        print(A[1])
    elif len(A[0])%2==0 and A[0]==[]:
        print("Fin")



X=[]
n = int(input("Número:"))
for i in range(n,0,-1):
    X.append(i)
print(X)
Y=[]
Z=[]
A=[X,Y,Z]
T=["X","Y","Z"]
print(T)

mov(A,0,0,T,0)
