codigodoaluno = int(input("Digite o código do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

maiornota = max(nota1, nota2, nota3)

media = (4 * maiornota + 3 * (nota1 + nota2 + nota3 - maiornota)) / 6

print("Código do aluno:", codigodoaluno)
print("Notas: {}, {}, {}".format(nota1, nota2, nota3))
print("Média: {:.2f}".format(media))

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")
