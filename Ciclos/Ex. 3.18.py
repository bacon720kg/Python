#    O Índice de massa corporal é um instrumento para determinar se uma pessoa está no peso ideal e é calculada pela divisão do peso, em quilogramas, do indivíduo pelo quadrado de sua altura, em metros, ou seja, IMC = Peso / (Altura * Altura).
#    Pelo IMC consegue-se saber qual a condição de uma pessoa:
#        IMC                    Condição
#        < 19.1                 Abaixo do peso
#        [19.1, 25.8[           No peso normal
#        [25.8, 27.3[           Marginalmente acima do peso
#        [27.3, 32.3[           Acima do peso ideal
#        >= 32.3                Obeso
#    Escreva um programa que, dado o nome, o peso em quilogramas e a altura em metros, de um número indeterminado de pessoas (terminar com o nome fim), calcule e escreva o IMC de cada pessoa, assim como a sua condição.
#    No fim, escreva o nome e IMC da pessoa com menor IMC, assim como a média de IMC's e as percentagens de cada uma das condições.

minimoimc = 10000
somaimc = 0
contapessoas = 0
contaabaixo = 0
contanormal = 0
contamaracima = 0
contaacimaid = 0
contaobeso = 0
nomemin = ""

print("Qual o nome da primeira pessoa? (Fim para terminar)")
nome = input()
while nome == "":
    print("Qual o nome da primeira pessoa? (Fim para terminar)")
    nome = input()

while nome != "Fim":
    contapessoas = contapessoas + 1

    print("Qual o seu peso em kg?")
    peso = int(input())
    while peso <= 0:
        print("Qual o seu peso em kg? O peso não pode ser menor ou igual a zero!")
        peso = int(input())

    print("Qual a sua altura em metros?")
    altura = float(input())
    while altura <= 0:
        print("Qual a sua altura em metros? A altura não pode ser menor ou igual a zero!")
        altura = float(input())

    imc = peso / altura ** 2

    somaimc = somaimc + imc

    if imc < 19.1:
        condi = "abaixo do peso"
        contaabaixo = contaabaixo + 1
    elif imc < 25.8:
        condi = "no peso normal"
        contanormal = contanormal + 1
    elif imc < 27.3:
        condi = "marginalmente acima do peso"
        contamaracima = contamaracima + 2
    elif imc < 32.3:
        condi = "acima do peso ideal"
        contaacimaid = contaacimaid + 1
    else:
        condi = "obeso"
        contaobeso = contaobeso + 1

    print("O seu IMC é", imc, "e está", condi, ".")

    if imc < minimoimc:
        minimoimc = imc
        nomemin = nome

    print("Qual o nome da próxima pessoa? (Fim para terminar)")
    nome = input()
    while nome == "":
        print("Qual o nome da próxima pessoa? (Fim para terminar)")
        nome = input()

if contapessoas == 0:
    print("Ninguém processado.")
else:
    print(nomemin, "é a pessoa com menor IMC.")
    print("A média de IMCS é", somaimc / contapessoas)
    print(contaabaixo / contapessoas * 100, "% das pessoas estão abaixo do peso.")
    print(contanormal / contapessoas * 100, "% das pessoas estão no peso normal.")
    print(contamaracima / contapessoas * 100, "% das pessoas estão marginalmente acima do peso.")
    print(contaacimaid / contapessoas * 100, "% das pessoas estão acima do peso ideal.")
    print(contaobeso / contapessoas * 100, "% das pessoas estão obesas.")
