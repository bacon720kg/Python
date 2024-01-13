# Leia uma lista de cinco números positivos e inteiros (Vetor A).

print("Leia uma lista de cinco números positivos e inteiros (Vetor A).")

A = [0, 0, 0, 0, 0]

for i in range(5):
    print("Qual o", i + 1, "º número?")
    A[i] = int(input())
    while A[i] <= 0:
        print("Qual o", i, "º número?")
        A[i] = int(input())

print("A =", A)


# Leia uma lista, de tamanho desconhecido, de números positivos e inteiros (Vetor B).
# A leitura termina quando aparece um -1. Assuma que o vetor B tem um tamanho máximo de 10.

print("")
print("Leia uma lista de tamanho desconhecido de números positivos e inteiros (Vetor B)")
print("A leitura termina quando aparece um -1. Assuma que o vetor B tem um tamanho máximo de 10.")

B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Qual o primeiro elemento? (-1 para terminar)")
B[0] = int(input())
while B[0] < -1:
    print("Qual o primeiro elemento? (-1 para terminar)")
    B[0] = int(input())

TamB = 0
while B[TamB] != -1 and TamB < 9:

    TamB = TamB + 1

    print("Qual o próximo elemento? (-1 para terminar)")
    B[TamB] = int(input())
    while B[TamB] < -1:
        print("Qual o próximo elemento? (-1 para terminar)")
        B[TamB] = int(input())

print("B =", B)


# Escreva a lista resultante da junção de A e B e coloque no vetor C.

print("")
print("Escreva a lista resultante da junção de A e B e coloque no vetor C.")

C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(5):
    C[i] = A[i]

for i in range(TamB):
    C[i + 5] = B[i]

TamC = 5 + TamB

print("C =", C)


# Escreva se existe um determinado número no vetor C e, caso exista, em que posição ocorre.

print("")
print("Escreva se existe um determinado número no vetor C e, caso exista, em que posição ocorre.")
print("Qual o número a procurar?")

Procura = int(input())
while Procura < 0:
    print("Qual o número a procurar?")
    Proc = int(input())

i = 0
while Procura != C[i] and i < TamC:
    i = i + 1

if Procura == C[i]:
    print("Número a procurar existe na posição", i + 1)
else:
    print("O número", Procura, "não existe em C")


# Escreva os números ímpares do vetor C.

print("")
print("Escreva os números ímpares do vetor C.")

for i in range(TamC):
    if C[i] % 2 != 0:
        print("C[", i + 1, "] = ", C[i])


# Escreva os números do vetor C pela ordem inversa à que foram inseridos.

print("")
print("Escreva os números do vetor C pela ordem inversa à que foram inseridos.")

for i in range(TamC - 1, -1, -1):
    print("C[", i + 1, "] =", C[i])


# Coloque no vetor D os elementos não repetidos do vetor C.

print("")
print("Coloque no vetor D os elementos não repetidos do vetor C.")

D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

TamD = 0
D[0] = C[0]
for i in range(1, TamC):
    D[TamD + 1] = C[i]

    K = 1
    while C[i] != D[K] and K < TamD + 1:
        K = K + 1

    if K == TamD + 1:
        TamD = TamD + 1

print("D =", D)
