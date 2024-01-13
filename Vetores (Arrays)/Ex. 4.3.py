# Uma unidade curricular tem como forma de avaliação os dois melhores de três testes.
# A leitura das notas de cada aluno é feita com o número do aluno e a nota que teve, terminando com a nota 0.
# Pretende-se um algoritmo que calcula e escreva:
#     • A nota de cada aluno;
#     • A média de cada um dos três testes.

Num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Nota = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

alunos = 0

for i in range(3):
    print("")
    print("*** Teste", i + 1, "***")

    print("Qual o número do primeiro aluno? (0 para terminar)")
    Num[alunos] = int(input())
    while Num[alunos] < 0:
        print("Qual o número do primeiro aluno? (0 para terminar)")
        Num[alunos] = int(input())

    while Num[alunos] != 0:
        k = 0
        while Num[alunos] != Num[k]:
            k = k + 1

        if alunos == k:
            alunos = alunos + 1
            Nota[k][0] = 0
            Nota[k][1] = 0
            Nota[k][2] = 0

        print("Nota?")
        Nota[k][i] = int(input())
        while 0 > Nota[k][i] > 20:
            print("Nota?")
            Nota[k][i] = int(input())

        print("Qual o número do próximo aluno? (0 para terminar)")
        Num[alunos] = int(input())
        while Num[alunos] < 0:
            print("Qual o número do próximo aluno? (0 para terminar)")
            Num[alunos] = int(input())

print("")
print("*** Notas de Alunos ***")
for i in range(alunos):
    max1 = 0
    max2 = 0
    for t in range(3):
        if Nota[i][t] > max1:
            max2 = max1
            max1 = Nota[i][t]
        elif Nota[i][t] > max2:
            max2 = Nota[i][t]
    notaf = (max1 + max2) / 2
    print(Num[i], "- Nota", notaf)

print("")
print("*** Média de testes ***")
for i in range(3):
    soma = 0
    conta = 0
    for j in range(alunos):
        if Nota[j][i] > 0:
            soma = soma + Nota[j][i]
            conta = conta + 1

    media = soma / conta
    print("Média do teste", i + 1, ":", media)
