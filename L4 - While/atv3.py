soma = 0
cont = 0
numero = 0

while cont < 50:
    if numero % 2 == 0:
        soma += numero
        cont += 1
    numero += 1

print("A soma dos 50 primeiros números pares é:", soma)
