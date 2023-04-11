numero = int(input("Digite um número no formato CDU: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

inverso = unidade * 100 + dezena * 10 + centena

print(f"Inverso={inverso}")
