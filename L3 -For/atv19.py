N = int(input("Digite um número inteiro: "))

primo = [True] * (N+1)
primo[0] = False
primo[1] = False
divisoes = 0

for i in range(2, N+1):
    if primo[i]:
        j = 2
        while i*j <= N:
            divisoes += 1
            primo[i*j] = False
            j += 1

print("Os números primos entre 1 e", N, "são:")
for i in range(2, n+1):
    if primo[i]:
        print(i)

print("O número de divisões realizadas foi:", divisoes)
