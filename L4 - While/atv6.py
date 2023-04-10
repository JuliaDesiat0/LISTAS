limiteinferior = float(input("Digite o limite inferior do intervalo: "))
limitesuperior = float(input("Digite o limite superior do intervalo: "))
decremento = float(input("Digite o decremento: "))

print("Celsius\tFahrenheit")
while limitesuperior >= limiteinferior:
    celsius = limitesuperior
    fahrenheit = (celsius * 9/5) + 32
    print("{:.1f}\t{:.1f}".format(celsius, fahrenheit))
    limitesuperior -= decremento