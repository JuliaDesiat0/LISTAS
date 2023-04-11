altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M/F): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Digite M para masculino ou F para feminino.")
    peso_ideal = None

if peso_ideal is not None:
    print("Seu peso ideal é:", round(peso_ideal, 2), "kg")
