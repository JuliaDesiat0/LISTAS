salariobruto = float(input("Digite o salário bruto do funcionário: "))
proventos = float(input("Digite o valor dos proventos: "))

if salariobruto <= 5000:
    desconto = salariobruto * 0.05
else:
    desconto = salariobruto * 0.1

salario_liquido = salariobruto + proventos - desconto
print("O salário líquido é R${:.2f}".format(salario_liquido))