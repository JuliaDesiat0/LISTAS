L = int(input("Digite o número de lados do polígono regular: "))
M = float(input("Digite a medida dos lados: "))

if L == 3:
    print("TRIANGULO")
    perimetro = 3 * M
    print("Perímetro: {:.2f}".format(perimetro))
elif L == 4:
    print("QUADRADO")
    area = M ** 2
    print("Área: {:.2f}".format(area))
elif L == 5:
    print("PENTAGONO")
elif L < 3:
    print("Não é polígono")
else:
    print("Polígono não identificado")
