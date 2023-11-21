maiorcliente = 0
nomemaiorcliente = ""
contaclientes = 0
somadospesos = 0

print("Qual o nome do 1º cliente? (Fim para terminar)")
nome = input()
while nome == "":
    print("Qual o nome do 1º cliente? (Fim para terminar)")
    nome = input()

while nome != "Fim" and nome != "fim":
    contaclientes = contaclientes + 1

    print("Quantas frutas diferentes comprou?")
    qtd = int(input())
    while qtd <= 0:
        print("Quantas frutas diferentes comprou?")
        qtd = int(input())

    paga = 0

    for i in range(qtd):
        print("Que fruta comprou: (B)ananas, (K)iwis, (L)aranjas ou (P)êssegos?")
        tipo = input()
        while tipo != "B" and tipo != "K" and tipo != "L" and tipo != "P":
            print("Que fruta comprou: (B)ananas, (K)iwis, (L)aranjas ou (P)êssegos?")
            tipo = input()

        print("Peso em kg?")
        peso = float(input())
        while peso <= 0:
            print("Peso?")
            peso = float(input())

        somadospesos = somadospesos + peso

        if tipo == "B":
            paga = paga + 0.99 * peso
        elif tipo == "K":
            paga = paga + 2.22 * peso
        elif tipo == "L":
            paga = paga + 1.25 * peso
        else:
            paga = paga + 1.75 * peso

    print(nome, "paga", paga, "euros.")

    if paga > maiorcliente:
        maiorcliente = paga
        nomemaiorcliente = nome

    print("Qual o nome do próximo cliente? (Fim para terminar)")
    nome = input()
    while nome == "":
        print("Qual o nome do próximo cliente? (Fim para terminar)")
        nome = input()

if contaclientes <= 0:
    print("Ninguém processado.")
else:
    print(nomemaiorcliente, "foi quem pagou mais (", maiorcliente, "euros).")
    print(contaclientes, "clientes foram processados.")
    print("Média de kg =", somadospesos / contaclientes)
