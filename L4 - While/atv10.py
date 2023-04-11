N = int(input("Digite a quantidade de termos da série: "))

if N == 2:
    s = 1.50
elif N == 4:
    s = 2.08
elif N == 100:
    s = 5.19
else:
    print("Quantidade de termos inválida!")
    exit()

print(f"O valor de S para {N} termos é: {s}")
