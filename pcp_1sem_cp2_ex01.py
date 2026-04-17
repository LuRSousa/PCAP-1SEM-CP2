#01. Sistema de Logistica

print('Bem-Vindo a central de Logistica')

#Recebe o peso em toneladas e passa para Kg
peso = int(input('Qual o peso do caminhão em toneladas: '))
kg = peso * 1000

#Recebe o codigo da carga que muda o valor da carga
codigo = int(input('Qual o codigo da carga de 10 a 40: '))
if 10 <= codigo <= 20:
    preco_kg = 100
elif 21 <= codigo <= 30:
    preco_kg = 250
elif 31 <= codigo <= 40:
    preco_kg = 340

#O total é o preço do codigo multiplicado pelo o Kg
total = kg * preco_kg

#A origem do caminhão muda o imposto que é pago sobre o total
origem = int(input('Qual a origem do caminhão de 1 a 5: '))
if origem == 1:
    imposto = 35
elif origem == 2:
    imposto = 25
elif origem == 3:
    imposto = 15
elif origem == 4:
    imposto = 5
elif origem == 5:
    imposto = 0

total_imposto = total * (imposto / 100)

#O valor total é o total da carga sem imposto mais o valor da carga com imposto
valor_total = total + total_imposto

print(f"Peso em kg: {kg}")
print(f"Preço da carga: R$ {total}")
print(f"Imposto: R$ {total_imposto}")
print(f"Valor total: R$ {valor_total}")

