A = int(input("Digite o ano: "))

if A % 400 == 0:
    print("O ano é bissexto")
elif A % 100 == 0:
    print("O ano não é bissexto")
elif A % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
