renda = int(input("Digite sua renda: "))
imposto = 0

if renda < 85528:
    imposto = ((renda * 0.18) - 556.02)
    valor = (round(imposto, 0))
    print("A taxa de impostos é: ", valor)
