#    Um grupo de cinco amigos vai organizar uma festa. Cada um deles leva vários artigos que podem ser: comida (C), bebidas (B) ou extras (E). Dado o nome do amigo e, para cada um deles, os artigos, o tipo desses artigos e o respetivo preço aproximado (a terminar com a letra F), apresente:
#        • Para cada amigo, a quantidade de artigos levados e, por tipo de artigo, a quantidade e o valor, assim como o valor total;
#        • O nome e a quantidade de artigos levados por quem levou mais artigos;
#        • O nome e o valor de artigos levado por quem levou mais em valor;
#        • As quantidades e valores totais de cada tipo de artigo.

topnumartigos = 0
topvalor = 0
numtotalcomida = 0
numtotalbebida = 0
numtotalextra = 0
somatotalcomida = 0
somatotalbebida = 0
somatotalextra = 0
nometopnum = ""
nometopvalor = ""

for i in range(5):
    print("Nome?")
    nome = input()
    while nome == "":
        print("Nome?")
        nome = input()

    contaartigos = 0
    contacomida = 0
    contabebida = 0
    contaextra = 0
    somacomida = 0
    somabebida = 0
    somaextra = 0

    print("Tipo do 1º artigo: (C)omida, (B)ebida ou (E)xtra? (F para terminar)")
    tipo = input()
    while tipo != "C" and tipo != "B" and tipo != "E" and tipo != "F":
        print("Tipo do 1º artigo: (C)omida, (B)ebida ou (E)xtra? (F para terminar)")
        tipo = input()

    while tipo != "F":
        contaartigos = contaartigos + 1

        print("Qual o preço aproximado desse artigo?")
        preco = int(input())
        while preco < 1:
            print("Qual o preço aproximado desse artigo?")
            preco = int(input())

        if tipo == "C":
            contacomida = contacomida + 1
            somacomida = somacomida + preco
        elif tipo == "B":
            contabebida = contabebida + 1
            somabebida = somabebida + preco
        else:
            contaextra = contaextra + 1
            somaextra = somaextra + preco

        print("Tipo do próximo artigo: (C)omida, (B)ebida ou (E)xtra? (F para terminar)")
        tipo = input()
        while tipo != "C" and tipo != "B" and tipo != "E" and tipo != "F":
            print("Tipo do próximo artigo: (C)omida, (B)ebida ou (E)xtra? (F para terminar)")
            tipo = input()

    if contaartigos > topnumartigos:
        topnumartigos = contaartigos
        nometopnum = nome

    if somacomida + somabebida + somaextra > topvalor:
        topvalor = somacomida + somabebida + somaextra
        nometopvalor = nome

    print("O", nome, "levou", contaartigos, "artigos")
    if contacomida > 0:
        print(contacomida, "comidas", somacomida, "euros")
    if contabebida > 0:
        print(contabebida, "bebidas", somabebida, "euros")
    if contaextra > 0:
        print(contaextra, "extras", somaextra, "euros")
    print("Total", somacomida + somabebida + somaextra, "euros")

    numtotalcomida = numtotalcomida + contacomida
    somatotalcomida = somatotalcomida + somacomida
    numtotalbebida = numtotalbebida + contabebida
    somatotalbebida = somatotalbebida + somabebida
    numtotalextra = numtotalextra + contaextra
    somatotalextra = somatotalextra + somaextra

print("O", nometopnum, "foi quem levou mais aritigos:", topnumartigos, ".")
print("O", nometopvalor, "foi quem levou mais em valor:", topvalor, "euros")
print(numtotalbebida, "bebidas,", numtotalcomida, "comidas e", numtotalextra, "extras, respetivamente", somatotalbebida, "euros ,", somatotalcomida, "euros e", somatotalextra, "euros.")
