dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print(f"{dia}/{mes}/{ano} não é uma data válida!")
else:
    if mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            diasnomes = 29
        else:
            diasnomes = 28
    elif mes in [4, 6, 9, 11]:
        diasnomes = 30
    else:
        diasnomes = 31
        
    if dia < 1 or dia > diasnomes:
        print(f"{dia}/{mes}/{ano} não é uma data válida!")
    else:
        print(f"{dia}/{mes}/{ano} é uma data válida!")
