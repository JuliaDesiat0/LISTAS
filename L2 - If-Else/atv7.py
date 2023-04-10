altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M/F): ")

if sexo == "M":
    pesoideal = (72.7 * altura) - 58
elif sexo == "F":
    pesoideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")
    pesoideal = None

if pesoideal is not None:
    print("Seu peso ideal é:", round(pesoideal, 2), "kg")