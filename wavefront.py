#Wavefront algorithm
#Yithzak Alarcón - T00045029
import numpy as np
print("Bienvenido")
print("\nIndica el tamaño de la matriz n (filas) x m (columnas): ")
n = int(input("\nEscriba el número de filas (n): "))
m = int(input("\nEscriba el número de columnas (m): "))
cont = 1
#Creación de matriz de prueba
A = np.zeros((n,m), int)
#Ingresamos números ordenados en la matriz para los obstaculos
for i in range (0,n):
    for j in range (0,m):
        A[i,j] = cont
        cont = cont +1
#Se muestra la matriz con su respectivo tamaño
print(A)
print("\nPor favor, selecciona los números en donde deseas los obstaculos:\n")
res = 's'
#Declaración de obstaculos
while res == 's' or res == 'S' or res == 'si' or res == 'Si':
    exp = int(input("\nDigite el número para colocar el obstaculo: "))
    for i in range (0,n):
        for j in range (0,m):
            if A[i,j] == exp:
                A[i,j] = -1
    
    print("\nLa matriz queda de la siguiente forma: \n", A)
    res = input("¿Desea continuar ingresando obstaculos? (s/n): ")
#Ingreso de coordenadas de inicio
ide_s = int(input("\nIngrese el número para colocar el inicio ('S'): "))
B = A

for i in range (0,n):
    for j in range (0,m):
        if B[i,j] == ide_s:
            B[i,j] = -2
            coor_s = np.array([i,j])
            start = np.array([i,j])
            print("\nCoordenadas: ", coor_s)

print(start)
#Ingreso de coordenadas de meta
ide_g = int(input("\nIngrese el número para colocar la meta ('G'): "))
for i in range (0,n):
    for j in range (0,m):
        if B[i,j] == ide_g:
            B[i,j] = -3
            coor_g = np.array([i,j])
            print("\nCoordenadas: ",coor_g)
print("\n\n",B)
#Matriz resultante con obstaculos e inicio-meta
for i in range (0,n):
    for j in range (0,m):
        if B[i,j] > 0:
            B[i,j] = 0
#Definición de puntos iniciales y finales        
B[coor_s[0], coor_s[1]] = 1
B[coor_g[0], coor_g[1]] = 0
print("\n",B)
asig = 0
#Definimos las funciones para la asignación de valores
def asignUp0(M, coor):
    if (M[coor[0]-1,coor[1]] == 0 and M[coor[0]-1,coor[1]] != -1 and M[coor[0]-1,coor[1]]<1):
        M[coor[0]-1,coor[1]] = M[coor[0],coor[1]] + 1
        V = [coor[0]-1]
        V += [coor[1]]
        return V
def asignDown0(M, coor):
    if (M[coor[0]+1,coor[1]] == 0 and M[coor[0]+1,coor[1]] != -1 and M[coor[0]+1,coor[1]]<1):
        M[coor[0]+1,coor[1]] = M[coor[0],coor[1]] + 1
        V = [coor[0]+1]
        V += [coor[1]]
        return V
def asignLeft0(M, coor):
    if (M[coor[0],coor[1]-1] == 0 and M[coor[0],coor[1]-1] != -1 and M[coor[0],coor[1]-1]<1):
        M[coor[0],coor[1]-1] = M[coor[0],coor[1]] + 1
        V = [coor[0]]
        V += [coor[1]-1]
        return V
def asignRight0(M, coor):
    if (M[coor[0],coor[1]+1] == 0 and M[coor[0],coor[1]+1] != -1 and M[coor[0],coor[1]+1]<1):
        M[coor[0],coor[1]+1] = M[coor[0],coor[1]] + 1
        V = [coor[0]]
        V += [coor[1]+1]
        return V
#Definimos los condicionales
def limit0(M, coor):
    global V,P
    if(coor[0]-1 >= 0 and M[coor[0]-1,coor[1]] == 0):
        a = asignUp0(M, coor)
        V += [a[0]]
        P += [a[1]]
    if(coor[0]+1 < n and M[coor[0]+1,coor[1]] == 0):
        b = asignDown0(M, coor)
        V += [b[0]]
        P += [b[1]]
    elif(coor[0]+1 < n and M[coor[0]+1,coor[1]] == None):
        input()
    if(coor[1]-1 >= 0 and M[coor[0],coor[1]-1] == 0):
        c = asignLeft0(M, coor)
        V += [c[0]]
        P += [c[1]]
    if(coor[1]+1 < m and M[coor[0],coor[1]+1] == 0):
        d = asignRight0(M, coor)
        V += [d[0]]
        P += [d[1]]
    elif(coor[1]+1 < m and M[coor[0],coor[1]+1] == None):
        input()
V = []
P =[]
#limit0(B, coor_s)
empty = False
apun = 1
ubiq = 0
while(empty == False):
    if(coor_s[0] == coor_g[0] and coor_s[1] == coor_g[1]):
        empty = True
    else:
        limit0(B, coor_s)
        print(B)
        coor_s[0] = V[ubiq]  
        coor_s[1] = P[ubiq]
        ubiq += 1
print(start)
print(B)
input()
X = []
Y = []
pts = coor_g
print(pts)
X += [pts[0]]
Y += [pts[1]]
conf = True
while(conf == True):    
    if(pts[0] != start[0] and pts[1] != start[1]):
        if(B[pts[0]-1,pts[1]] < B[pts[0],pts[1]] and B[pts[0]-1,pts[1]] != -1 and B[pts[0]-1,pts[1]] != 0 and pts[0]-1 >= 0):
            pts[0] = pts[0] - 1
            X += [pts[0]]
            Y += [pts[1]]
            print("\n1.")
        elif(B[pts[0]+1,pts[1]] < B[pts[0],pts[1]] and B[pts[0]+1,pts[1]] != -1 and B[pts[0]+1,pts[1]] != 0 and pts[0]+1 < n):
            X += [pts[0]]
            Y += [pts[1]]
            print("\n2.")
        elif(B[pts[0],pts[1]-1] < B[pts[0],pts[1]] and B[pts[0],pts[1]-1] != -1 and B[pts[0],pts[1]-1] != 0 and pts[1]-1 >= 0):
            pts[1] = pts[1] - 1
            X += [pts[0]]
            Y += [pts[1]]
            print("\n3.")
        elif(B[pts[0],pts[1]+1] < B[pts[0],pts[1]] and B[pts[0],pts[1]+1] != -1 and B[pts[0],pts[1]+1] != 0 and pts[1]+1 < m):
            pts[0] = pts[1] + 1
            X += [pts[0]]
            Y += [pts[1]]
            print("\n4.")
        elif(B[pts[0]+1,pts[1]] == None or B[pts[0],pts[1]+1] == None):
            input()
        else:
            print("\n¡Fin!")
    elif(pts[0] == start[0] and pts[1] == start[1]):
        conf = False

print(start)
print(X)
print(Y)
print("Game Over")
#def mirar(p_in, M):
    
    
    