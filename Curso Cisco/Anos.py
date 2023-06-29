year = int(input("Digite um ano: "))

if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    if year % 4 != 0:   #Verifica se é divisível por 4
        print("ano comum")
    elif year % 100 != 0:   #Verifica se é divisível por 100
        print("Ano bissexto")
    elif year % 400 != 0:   #Verifica se é divisível por 400
        print("ano comum")
    else:
        print("Ano bissexto")

