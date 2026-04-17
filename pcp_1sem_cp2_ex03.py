#03. Sistema de calculo de médias do aluno

#Definindo as variáveis das notas
cp1 = (float(input ("Digite qual é sua nota da cp1: ")))
cp2 = (float(input ("Digite qual é sua nota da cp2: ")))
cp3 = (float(input ("Digite qual é sua nota da cp3: ")))
sp1 = (float(input ("Digite qual é sua nota da sp1: ")))
sp2 = (float(input ("Digite qual é sua nota da sp2: ")))
gs = (float(input ("Digite qual é sua nota da gs: ")))

#Descartando a menor nota
menor = 0

if cp1 < cp2 and cp1 < cp3:
    menor = cp1
elif cp2 < cp1  and cp2 < cp3:
    menor = cp2
elif cp3 < cp1 and cp3 <cp2:
    menor = cp3
    
#Calculo da média do aluno
media = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + gs * 0.6

#Mostrando resultados
print("Essa é sua média:")
print(f"{media:.1f}")

media_peso = 0.4 * media
print("Sua media peso:")
print(f"{media_peso:.1f}")

