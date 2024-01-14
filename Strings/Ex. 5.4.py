# Escreva o número de vogais de um texto.

vogais = "aeiou"

print("Introduza um texto.")
texto = input()
while texto == "":
    print("Introduza um texto.")
    texto = input()

conta = 0

for i in range(len(texto)):
    car = texto[i]

    onde = vogais.find(car)

    if onde != -1:
        conta = conta + 1

if conta > 0:
    print("O texto tem", conta, "vogais.")
else:
    print("O texto não tem vogais.")
