# Dado um texto, conte e escreva o número de vezes que cada letra aparece.

F = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

alfa = "abcdefghijklmnopqrstuvwxyz"

print("Introduza o texto.")
texto = input()
while texto == "":
    print("Introduza o texto.")
    texto = input()

for i in range(len(texto)):
    car = texto[i]

    onde = alfa.find(car)

    if onde != -1:
        F[onde] = F[onde] + 1

for i in range(26):
    if 0 < F[i] < 2:
        print("A letra", alfa[i], "aparece", F[i], "vez.")
    elif F[i] > 1:
        print("A letra", alfa[i], "aparece", F[i], "vezes.")
