# Main
N = int(input())
S = list(map(int, input().split()))
D = int(input())

sides = []
conjuntos = []
valores = []
suma = []

for _ in range(D):
    L, R, V = map(int, input().split())
    sides.append([L, R, V])

valores.append(sides[0][2])
conjuntos.append([sides[0][0], sides[0][1]])
sides.pop(0)

i = 0
anterior = len(conjuntos[i])
while(len(sides) != 0):
    for x in sides:
        if len(conjuntos[i]) == 0:
            valores[i] += x[2]
            conjuntos[i].append(x[0])
            conjuntos[i].append(x[1])
            sides.remove(x)
        elif(x[0]>=min(conjuntos[i]) and x[0]<=max(conjuntos[i])) or (x[1]>=min(conjuntos[i]) and x[1]<=max(conjuntos[i])):
            valores[i] += x[2]
            conjuntos[i].append(x[0])
            conjuntos[i].append(x[1])
            sides.remove(x)
    actual = len(conjuntos[i])
    if anterior == actual:
        conjuntos.append([])
        valores.append(0)
        i+=1
    anterior = actual


for y in conjuntos:
    temp = 0
    for j in range(min(y)-1, max(y)):
        temp += S[j]
    suma.append(temp)

ans = 0

for z in range(len(suma)):
    if suma[z] <= valores[z]:
        ans += suma[z]
    else:
        ans += valores[z]

print(ans)