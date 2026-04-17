#02. Sistema de verificação de triângulo com base nos 3 lados

#Definindo o tamanho dos lados dos triangulos
ladoA = int(input("Digite o primeiro lado do triângulo: "))
ladoB = int(input("Digite o segundo lado do triângulo: "))
ladoC = int(input("Digite o terceiro lado do triângulo: "))

#Comparando o menor lado
if (ladoB > ladoA):
    aux = ladoB
    ladoB = ladoA
    ladoA = aux
if (ladoC > ladoA):
    aux = ladoC
    ladoC = ladoA
    ladoA = aux

#Calculando o tipo de triângulo pelo ângulo
def calcular_angulo(a, b, c):
    if (a >= b + c):
        print("Não forma triângulo.")
    elif (a ** 2 == b ** 2 + c ** 2):
        print("Triângulo Retângulo")
    elif (a ** 2 > b ** 2 + c ** 2):
        print("Triângulo Obtusângulo")
    elif (a ** 2 < b ** 2 + c ** 2):
        print("Triângulo Acutângulo")

#Calculando o tipo de triângulo pelo lado
def calcular_lados(a, b, c):
    if (a >= b + c):
        print("Não forma triângulo.")
    elif (a == b and b == c):
        print("Triângulo Equilátero")
    elif (a == b or a == c or b == c):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

#Mostrando resultados
calcular_angulo(ladoA, ladoB, ladoC)
calcular_lados(ladoA, ladoB, ladoC)
