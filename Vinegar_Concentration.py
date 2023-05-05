C_NaOH = float(input("Concentração do NaOH: "))

m = 6 * C_NaOH / 1000

uAcido = m * 250 / 25

percentualAcido = uAcido * 100 / 25

print(f"Concentração Percentual do Ácido Acético: {percentualAcido:.2f}%")
