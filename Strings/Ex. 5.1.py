# Escreva todas as letras de um texto.

alfa = "abcdefghijklmnopqrstuvwxyz"

print("Introduza um texto.")
texto = input()
while texto == "":
    print("Introduza um texto.")
    texto = input()

for i in range(len(texto)):
    car = texto[i]

    onde = alfa.find(car)

    if onde != -1:
        print(car)
