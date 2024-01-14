# Descodifique um texto, substituindo cada caráter por outro que se situe cinco posições atrás no alfabeto.

alfa = "abcdefghijklmnopqrstuvwxyz "

print("Introduza um texto.")
texto = input()
while texto == "":
    print("Introduza um texto.")
    texto = input()

codigo = ""

for i in range(len(texto)):
    car = texto[i]

    onde = alfa.find(car)

    if onde - 5 < 0:
        codigo = codigo + alfa[onde - 5 + 27]
    else:
        codigo = codigo + alfa[onde - 5]

print(codigo)
