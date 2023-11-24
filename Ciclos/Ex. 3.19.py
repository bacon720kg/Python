# A nota de uma unidade curricular é obtida a partir de um conjunto de parcelas. Uma dessas parcelas é a nota de aulas, apenas para alunos que foram a pelo menos 75% das aulas, e que é constituída pelos três melhores testes de um máximo de cinco. E segundo a tabela seguinte:
#    Média        Nota
#    [0, 5[       0
#    [5, 10[      1
#    [10, 15[     2
#    [15, 20]     3
# Pretende-se um algoritmo que, para uma turma com um número conhecido de alunos, calcula e escreva para cada: se tiver nota de aulas, o seu valor e a média dos testes, caso contrário a mensagem "não tem assiduidade, logo a sua nota é 0.", assim como o nome e a nota do aluno que teve melhor nota e a média das médias da turma, apenas para os que tem assiduidade.

melhornota = 0
contacomassid = 0
contasemassid = 0
somadasmedias = 0
melhoraluno = ""

print("Quantos alunos são?")
num = int(input())
while num <= 0:
    print("Quantos alunos são?")
    num = int(input())

for i in range(num):
    print("Qual o nome do", i + 1, "º aluno?")
    nome = input()
    while nome == "":
        print("Qual o nome do", i + 1, "º aluno?")
        nome = input()

    print("Qual a percentagem da sua assiduidade? (Escreva apenas números sem o símbolo %)")
    per = int(input())
    while per < 0 or per > 100:
        print("Qual a percentagem da sua assiduidade? (Escreva apenas números sem o símbolo %)")
        per = int(input())

    if per < 75:
        print(nome, "não tem assiduidade, logo a sua nota é 0.")
        contasemassid = contasemassid + 1
    else:
        contacomassid = contacomassid + 1

        print("Quantos testes fez? (0 a 5)")
        testes = int(input())
        while testes < 0 or testes > 5:
            print("Quantos testes fez? (0 a 5)")
            testes = int(input())

        melhor1 = 0
        melhor2 = 0
        melhor3 = 0

        for x in range(testes):
            print("Qual a nota do", x + 1, "º teste? (0 a 20)")
            nota = int(input())
            while nota < 0 or nota > 20:
                print("Qual a nota do", x + 1, "º teste? (0 a 20)")
                nota = int(input())

            if nota > melhor1:
                melhor3 = melhor2
                melhor2 = melhor1
                melhor1 = nota
            elif nota > melhor2:
                melhor3 = melhor2
                melhor2 = nota
            elif nota > melhor3:
                melhor3 = nota

        media = (melhor1 + melhor2 + melhor3) / 3
        somadasmedias = somadasmedias + media

        if media < 5:
            cat = 0
        elif media < 10:
            cat = 1
        elif media < 15:
            cat = 2
        else:
            cat = 3

        print(nome, "tem média de", media, ", logo a nota é", cat, ".")

        if media > melhornota:
            melhornota = media
            melhoraluno = nome

print("Há", contacomassid, "alunos com assiduidade e", contasemassid, "sem assiduidade.")
print("O", melhoraluno, "teve", melhornota, ", foi o melhor.")
print("A média da turma é", somadasmedias / contacomassid, ".")
