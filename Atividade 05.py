# 5 - Programação que receba dois números inteiros 
def soma(a,b):
    return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  resultado = 0
  negativo = False
  if b < 0:
    b = -b
    negativo = True

  for i in range(b):
    resultado = soma (resultado, a )

  if negativo:
    resultado = -resultado

  return resultado

def pontecia(a, b):
  if b == 0:
    return 1
  elif b < 0:
    return " não é possível calcular potencia com  expoente negativo"

  resultado = 1
  for i in range(b):
    resultado = multiplicacao (resultado, a)

  return resultado

def main():
  print(" === Caculadora básica ===")
  a = int(input("Digite o primeiro número:"))
  b = int(input("Digite o segundo número:"))

  print("\nescolha a operação:")
  print("1 - soma")
  print("2 - subtracao")
  print("3 - multiplicacao")
  print("4 - potencia")

  Escolha = int(input("digite qual opção:"))

  if Escolha == 1:
    print("resultado:", soma(a,b))
  elif Escolha == 2:
    print("resultado:", subtracao(a,b))
  elif Escolha == 3:
    print("resultado:", multiplicacao(a,b))
  elif Escolha == 4:
    print("resultado:", pontecia(a,b))
  else:
    print("Escolha inválida!")

if __name__ == "__main__":
  main()
