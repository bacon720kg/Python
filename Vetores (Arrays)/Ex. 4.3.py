# Uma unidade curricular tem como forma de avaliação os dois melhores de três testes.
# A leitura das notas de cada aluno é feita com o número do aluno e a nota que teve, terminando com a nota 0.
# Pretende-se um algoritmo que calcula e escreva:
#   • A nota de cada aluno;
#   • A média de cada um dos três testes.

Num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Nota = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

Alunos = 0

for i in range(3):
    print("")
    print("*** Teste", i + 1, "***")

    print("Qual o número do primeiro aluno? (0 para terminar)")
    Num[Alunos] = int(input())
    while Num[Alunos] < 0:
        print("Qual o número do primeiro aluno? (0 para terminar)")
        Num[Alunos] = int(input())

    while Num[Alunos] != 0:
        k = 0
        while Num[Alunos] != Num[k]:
            k = k + 1

        if Alunos == k:
            Alunos = Alunos + 1
            Nota[k][0] = 0
            Nota[k][1] = 0
            Nota[k][2] = 0

        print("Nota?")
        Nota[k][i] = int(input())
        while 0 > Nota[k][i] > 20:
            print("Nota?")
            Nota[k][i] = int(input())

        print("Qual o número do próximo aluno? (0 para terminar)")
        Num[Alunos] = int(input())
        while Num[Alunos] < 0:
            print("Qual o número do próximo aluno? (0 para terminar)")
            Num[Alunos] = int(input())

print("")
print("*** Notas de Alunos ***")
for i in range(Alunos):
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
    Soma = 0
    Conta = 0
    for j in range(Alunos):
        if Nota[j][i] > 0:
            Soma = Soma + Nota[j][i]
            Conta = Conta + 1

    Media = Soma / Conta
    print("Média do teste", i + 1, ":", Media)
