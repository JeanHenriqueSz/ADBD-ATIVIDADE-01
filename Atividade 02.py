#2.1 - Receba do usuário 10 números inteiros e coloque em uma estrutura de dados.
numeros = []

for numero in range(10):
    numero = int(input(f'Digite o {numero + 1}° numero inteiro: '))
    numeros.append(numero)
    
#2.3 - Na sequência solicite ao usuário que informe um novo número inteiro, e verifique se este número encontra-se registrado.

numeroDois = int(input(f'\nDigite o numero para comparar: '))


if numeroDois in numeros:
    print('\nEste numero está registrado')
    
if numeroDois not in numeros:
    print('\nEste numero não está registrado')

#2.4 - Caso positivo, imprima a(s) posição(ões) em que este número estiver na estrutura. Caso contrário, exiba uma mensagem avisando ao usuário informando que o número não se encontra na estrutura.
for indice, numero in enumerate(numeros):
    if numero == numeroDois:
        print(f"\nA posição que o numero está é a: {indice}")
    
        
