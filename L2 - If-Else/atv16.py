lados = int(input("Digite o número de lados do polígono regular: "))
medida = float(input("Digite a medida dos lados: "))

if lados == 3:
    print("TRIANGULO")
    perimetro = 3 * medida
    print("Perímetro: {:.2f}".format(perimetro))
elif lados == 4:
    print("QUADRADO")
    area = medida ** 2
    print("Área: {:.2f}".format(area))
elif lados == 5:
    print("PENTAGONO")
elif lados < 3:
    print("Não é polígono")
else:
    print("Polígono não identificado")