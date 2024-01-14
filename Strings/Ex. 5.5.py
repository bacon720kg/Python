# Dado um nome completo, converta-o no seguinte formato: (último nome), (primeiro nome) (iniciais dos restantes.).

print("Introduza um nome completo.")
nome = input()
while nome == "":
    print("Introduza um nome completo.")
    nome = input()

esp = nome.find(" ")

first = nome[0:esp]

novo = first

nome = nome[esp + 1:len(nome)]

esp = nome.find(" ")

while esp != -1:
    novo = novo + " " + nome[0] + "."

    nome = nome[esp + 1:len(nome)]

    esp = nome.find(" ")

novo = nome + ", " + novo
print(novo)
