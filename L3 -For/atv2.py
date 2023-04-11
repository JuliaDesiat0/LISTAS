l = int(input("Digite o número de linhas da matriz: "))
c = int(input("Digite o número de colunas da matriz: "))

# construção e impressão da matriz
for i in range(l):
  for j in range(c):
    print(f"A{i},{j}", end="")
    if j == c-1:
      print("#", end="")
    else:
      print(" ", end="")
  print()

