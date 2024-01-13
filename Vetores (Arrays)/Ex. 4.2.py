# Considera a seguinte função:
#        { |x| para x < 0
# F(x) = { 0 para x = 0
#        { x! para x > 0
# Elabore um algoritmo para:
#     • Calcular e escrever F(x), sendo x inteiro e pertencente ao intervalo [-a, a], em que a é inteiro e positivo;
#     • Calcular e escrever a média dos valores de F(x) em [-a, a];
#     • Escrever, de forma decrescente, os valores de F(x) maiores que a média.

F = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Qual o limite superior?")
a = int(input())
while a <= 0:
    print("Qual o limite superior?")
    a = int(input())

Soma = 0
for x in range(-a, a + 1):
    if x < 0:
        F[x] = abs(x)
    elif x == 0:
        F[x] = 0
    else:
        F[x] = 1
        for i in range(x, 1, -1):
            F[x] = F[x] * i
    print("F(", x, ") =", F[x])

    Soma = Soma + F[x]

Media = Soma / (2 * a + 1)
print("A média de F(x) é", Media)

for x in range(a, -a, -1):
    if F[x] > Media:
        print("F(", x, ") =", F[x], ">", Media)
