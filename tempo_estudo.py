tempo=int(input("quantas horas o usuario estuda por dia?"))
if tempo<=2:
    print("pouco estudo")
elif tempo <=4:
    print("estudo medio")
elif tempo >4:
    print("muito estudo")
else:
    print("erro de digitação")