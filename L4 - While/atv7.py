josberanilsonaltura = 1.5
apricocildoaltura = 1.1
anos = 0

while apricocildoaltura <= josberanilsonaltura:
    anos += 1
    josberanilsonaltura += 0.02
    apricocildoaltura += 0.03
    print(f"Ano {anos}: Josberanilson {josberanilsonaltura:.2f}m, Apricoçildo {apricocildoaltura:.2f}m")

print(f"Apricoçildo ultrapassou Josberanilson após {anos} anos.")