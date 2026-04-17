#05. Sistema de banco que calcula o valor da parcela fixa de um financiamento

#Definindo variáveis
nome = input("Digite o seu nome completo: ")
idade = int(input("Digite sua idade: "))
renda_mes = float(input("Digite sua renda mensal: "))
valor_empr = float(input("Digite o valor do empréstimo: "))
parcelas = int(input("Digite a quantidade de parcelas que deseja: "))

#Calculando taxas pelo número de parcelas
def taxas(parcelas):
    if parcelas<=6:
        return 0.05
    elif parcelas>6 and parcelas<=12:
        return 0.08
    else:
        return 0.1 
    
valor_taxa = taxas(parcelas)

#Calculando o valor da parcela
def valor_da_parcela():
    PMT = valor_empr*((valor_taxa*(1+valor_taxa)**parcelas)/((1+valor_taxa)**parcelas-1))
    return PMT

PMT = valor_da_parcela()

#Cálculos
lim_aprovacao = 20*renda_mes
total = PMT * parcelas
if valor_empr>total:
    juros_pagos = valor_empr - total
else:
    juros_pagos = total - valor_empr

#Mostrando os resultados
print("Bem-vindo ao sistema de empréstimos")
print("-----------------------------------")

if idade>=18 and valor_empr<=lim_aprovacao:
    print("Seu emprétimo foi aprovado")
    print (f"O(a) sr.(sra.) {nome}")
    print (f"Financiou R${valor_empr:.2f}")
    print (f"com uma taxa de juros de {valor_taxa * 100}%")
    print (f"E o valor da parcela vai ser R${PMT:.2f}")
    print (f"O valor total pago é R${total:.2f}")
    print (f"O valor total de juros pagos R${juros_pagos:.2f}")
elif idade<18:
    print("Seu empréstimo foi negado por ser menor de idade")
else:
    print("Seu empréstimo foi negado por empréstimo ultrapassar limite de aprovação")
