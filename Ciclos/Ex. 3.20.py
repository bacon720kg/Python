# Uma frutaria vende quatro tipos de frutas: Bananas, Kiwis, Laranjas e Pêssegos (respetivamente 0.99€, 2.22€, 1.25€ e 1.75€ por kg) e pretende um programa que:
#     • Para cada cliente leia o nome, o número de frutas que comprou, a quantidade de cada uma e calcule o preço a pagar;
#     • No fim do dia (que termina com o cliente "fim"), escreva o nome do cliente que mais pagou (assim como o valor pago), quantos clientes foram proces-sados e qual foi a média em kg.

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
