
sp=67836.43
rj=36678.66
mg=29229.88
es=27165.48
outros=19849.53

faturamentoTotal = sp + rj + mg + es + outros

def porcentagem(cidade):
    return (cidade*100)/faturamentoTotal

print(faturamentoTotal)

print(f"São Paulo ficou com %{porcentagem(sp)}")
print(f"Rio de Janeiro ficou com %{porcentagem(rj)}")
print(f"Minas Gerais ficou com %{porcentagem(mg)}")
print(f"Espirito Santo ficou com %{porcentagem(es)}")
print(f"Outros ficou com %{porcentagem(outros)}")
