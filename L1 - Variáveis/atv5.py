num = int(input("Digite um número no formato CDU: "))

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

inverso = unidade * 100 + dezena * 10 + centena

print(f"Inverso={inverso}")
