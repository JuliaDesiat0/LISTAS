idade = int(input("Insira a idade do nadador: "))

if idade >= 5 and idade <= 7:
    categoria = "infantil a"
elif idade >= 8 and idade <= 10:
    categoria = "infantil b"
elif idade >= 11 and idade <= 13:
    categoria = "juvenil a"
elif idade >= 14 and idade <= 17:
    categoria = "juvenil b"
else:
    categoria = "sênior"

print("O nadador se enquadra na categoria", categoria)
