#4.1 - Solicite ao usuário que informe inicialmente os 6 números sorteados na Mega Sena.
numeros = []
numerosJogados= []

for numero in range(6):
    numero = int(input(f"Digite o {numero+1}° numero sorteado na mega sena: "))
    numeros.append(numero)


#4.2 - Em seguida, peça que ele digite os 6 números do cartão que jogou.
for numero in range(6):
    numero = int(input(f"Digite o {numero+1}° numero que você marcou: "))
    numerosJogados.append(numero)


#4.3 - Imprima a quantidade de pontos que ele fez no concurso.
total = 0

for item in numerosJogados:
    if item in numeros:
        total += 1
    
print(f"Você acertou {total} pontos na mega sena")