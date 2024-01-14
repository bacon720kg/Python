# Escreva o número de vezes que uma palavra aparece num texto.

print("Introduza um texto.")
texto = input()
while texto == "":
    print("Introduza um texto.")
    texto = input()

print("Introduza a palavra a procurar.")
proc = input()
while proc == "":
    print("Introduza a palavra a procurar.")
    proc = input()

texto = texto + " "

contador = 0

onde = texto.find(proc + " ")
while onde != -1:
    contador = contador + 1

    texto = texto[onde + len(proc):len(texto)]

    onde = texto.find(proc + " ")

if contador > 0:
    print("A palavra", proc, "aparece", contador, "vez(es) no texto.")
else:
    print("A palavra não aparece no texto.")
