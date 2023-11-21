# A avaliação de uma unidade curricular tem como base cinco minitestes ao longo do semestre. Dado o número, nome, número de minitestes feitos e nota de cada miniteste de um número indeterminado de alunos (a terminar com um número 0), pretende-se calcular e escrever:
#    • A nota final de cada um dos alunos, de acordo com a fórmula:
#        Nota final = 50% melhor miniteste + 50% média dos restantes minitestes
#    • O resultado de cada aluno, de acordo com a seguinte tabela:
#        Nota Final    Resultado
#        [0, 8[        Reprovado
#        [8, 12[       Oral
#        [12, 20]      Aprovado
#    • O nome e nota final do aluno com a melhor nota final;
#    • A média das notas finais dos alunos processados;
#    • A percentagem de alunos por resultado (Reprovado, Oral e Aprovado).

melhornotafinal = 0
somanotasfinais = 0
contaalunos = 0
contarep = 0
contaoral = 0
contaaprov = 0
melhornome = ""

print("Qual o seu número de aluno? (0 para terminar)")
num = int(input())
while num < 0:
    print("Qual o seu número de aluno? (0 para terminar)")
    num = int(input())

while num != 0:
    contaalunos = contaalunos + 1
    print("Qual o seu nome?")
    nome = input()
    while nome == "":
        print("Qual o seu nome?")
        nome = input()
    print("Quantos testes fez o aluno", num, "-", nome, "? (1 a 5)")
    qtd = int(input())
    while qtd < 1 or qtd > 5:
        print("Quantos testes fez o aluno", num, "-", nome, "? (1 a 5)")
        qtd = int(input())

    melhornotaaluno = 0
    somanotasaluno = 0
    for i in range(qtd):
        print("Qual a nota do aluno", num, "-", nome, "no teste", i + 1, "? (0 a 20)")
        nota = int(input())
        while nota < 0 or nota > 20:
            print("Qual a nota do aluno", num, "-", nome, "no teste", i + 1, "? (0 a 20)")
            nota = int(input())

        somanotasaluno = somanotasaluno + nota

        if nota > melhornotaaluno:
            melhornotaaluno = nota
    if qtd > 1:
        notafinal = melhornotaaluno * 0.5 + ((somanotasaluno - melhornotaaluno) / (qtd - 1)) * 0.5
    else:
        notafinal = melhornotaaluno * 0.5 + 0 * 0.5
    print(num, "-", nome, "teve nota final", notafinal)

    if notafinal > melhornotafinal:
        melhornotafinal = notafinal
        melhornome = nome

    if notafinal < 8:
        print("Reprovado")
        contarep = contarep + 1
    elif notafinal < 12:
        print("Oral")
        contaoral = contaoral + 1
    else:
        print("Aprovado")
        contaaprov = contaaprov + 1

    somanotasfinais = somanotasfinais + notafinal

    print("Qual o seu número de aluno? (0 para terminar)")
    num = int(input())
    while num < 0:
        print("Qual o seu número de aluno? (0 para terminar)")
        num = int(input())

if contaalunos > 0:
    print("O aluno", melhornome, "teve a melhor nota =", melhornotafinal)
    media = somanotasfinais / contaalunos
    print("Média de notas =", media)
    paprov = contaaprov / contaalunos * 100
    poral = contaoral / contaalunos * 100
    prep = contarep / contaalunos * 100
    print(paprov, "% Aprovados", poral, "Oral", prep, "Reprovados")
else:
    print("Ninguém processado")
