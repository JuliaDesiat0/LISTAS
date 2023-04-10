limiteinferior = int(input("Digite o limite inferior: "))
limitesuperior = int(input("Digite o limite superior: "))
incremento = int(input("Digite o incremento: "))

for num in range(limiteinferior, limitesuperior+1, incremento):
    print(num)