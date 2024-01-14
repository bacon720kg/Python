# Dado um texto sem sinais de pontuação, inverta cada uma das palavras do texto.

alfa = "abcdefghijklmnopqrstuvwxyz"

print("Introduza um texto.")
texto = input()
while texto == "":
    print("Introduza um texto.")
    texto = input()

texto = texto + " "

inv = ""

esp = texto.find(" ")
while esp != -1:
    pal = texto[0:esp]

    for i in range(len(pal) - 1, -1, -1):
        car = pal[i]

        inv = inv + car

    inv = inv + " "

    texto = texto[esp + 1:len(texto)]

    esp = texto.find(" ")

print(inv)
