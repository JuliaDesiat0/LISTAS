limitesuperior = int(input("Digite o limite superior do intervalo desejado: "))
incremento = int(input("Digite o incremento desejado: "))
limiteinferior = 10

print("Fahrenheit \t Celsius")
for f in range(limiteinferior, limitesuperior + 1, incremento):
    c = round((f - 32) * 5 / 9, 2)
    print("{:.2f}F \t\t {:.2f}C".format(f, c))

