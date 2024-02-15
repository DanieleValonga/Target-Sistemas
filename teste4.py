faturamento_total = 67836.43 + 36678.66 + 29229.88 + 27165.48 + 19849.53

estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

for estado, faturamento in estados.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
