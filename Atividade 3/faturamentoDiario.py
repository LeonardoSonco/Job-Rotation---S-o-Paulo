import json

with open('dados.json') as file:
    data = json.load(file)

faturamento = []
diasAcimaMedia = 0
for dia in data:
    if 'valor' in dia:
        # Verifica se o há valor
        if dia['valor'] is not None:
            # Adicione o valor 'valor' à lista de faturamento
            faturamento.append(dia['valor'])

menorFaturamento = min(faturamento)
maiorFaturamento = max(faturamento)
mediaMensal = sum(faturamento) / len(faturamento)

for value in faturamento:
    if value > mediaMensal:
        diasAcimaMedia += 1

print(f"Menor valor: {menorFaturamento}")
print(f"Maior valor: {maiorFaturamento}")
print(f"Maior valor: {mediaMensal}")
print(f"Numero de dias acima da media: {diasAcimaMedia}")
