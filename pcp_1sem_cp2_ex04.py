#04. Sistema de RH que calcula salário final de um funcionário com base em: cargo, horas extras, faltas, bônus e descontos
 
#Definindo variáveis
nome_func = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o número do respectivo cargo do funionário: \n 1- Gerente \n 2- Analista \n 3- Assistente \n 4- Estagiário \n"))
salario_base = float(input("Digite o salário base do funcionário: R$"))
horas = int(input("Digite o total de horas extras trabalhadas pelo funcionário: "))
falta_mes = int(input("Digite o total de faltas do funcionário no mês: "))
recebeu_bonus = input("Digite se o funcionário recebeu bônus de desempenho 's' para Sim ou 'n' para Não:")
recebeu_bonus = recebeu_bonus.lower()
 
#Calculando horas extras e descontos com base no salário base e taxa
def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas
 
def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

#Calculando o bônus que varia com o cargo
def calcular_bonus(cargo, recebeu_bonus):
    match cargo:
        case 1:
            return 1000
        case 2:
            return 500
        case 3:
            return 300
        case 4:
            return 100
        case _:
            return 0

#Cálculos          
horas_extras = calcular_horas_extras(salario_base, horas)
descontos_faltas = calcular_descontos_faltas(salario_base, falta_mes)

if recebeu_bonus == 's':
    bonus = calcular_bonus(cargo, recebeu_bonus)
else:
    bonus = 0
 
acrescimos = horas_extras + bonus
salario_bruto = salario_base + acrescimos
salario_final = salario_bruto - descontos_faltas
 
#Mostrando resultados
print(f"\nFuncionário(a) {nome_func}:")
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Acréscimos (horas extras + bônus): R${acrescimos:.2f}")
print(f"Descontos (p/ falta): R${descontos_faltas:.2f}")
print(f"Salário final: R${salario_final:.2f}")
