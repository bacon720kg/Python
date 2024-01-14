# Dado um texto, conte e escreva o número de vezes que cada palavra aparece.

F = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
P = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

print("Introduza o texto.")
texto = input()
while texto == "":
    print("Introduza o texto.")
    texto = input()

texto = texto + " "

conta = 0

esp = texto.find(" ")
while esp != -1:
    pal = texto[0:esp]

    P[conta + 1] = pal
    F[conta + 1] = 1
    k = 0
    while P[k] != pal:
        k = k + 1
    if k <= conta:
        F[k] = F[k] + 1
    else:
        conta = conta + 1

    texto = texto[esp + 1:len(texto)]

    esp = texto.find(" ")

for i in range(conta + 1):
    if F[i] == 1:
        print(P[i], "aparece", F[i], "vez.")
    elif F[i] > 1:
        print(P[i], "aparece", F[i], "vezes.")
