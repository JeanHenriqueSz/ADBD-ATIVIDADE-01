# 3.1 - receber 10 numeros inteiros  e guarda em linha 
números = []
for i in range(10):
  while True:
    num_str = input(f"Digite o número {i + 1}:")
    num_str_cleaned = num_str.replace(" ", "")
    try:
      num = int(num_str_cleaned)
      números.append(num)
      break 
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro válido.")

# 3.2 - trocar todos os valores negativos por 0
for i in range(len(números)):
  if números[i] < 0:
    números[i] = 0

# 3.3 - imprimir o resultados dos dados alterados ]
print("\números alterados:")
print(números)
