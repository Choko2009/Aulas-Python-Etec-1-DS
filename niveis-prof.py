import os
os.system("cls")

nivel=int(input("digite o nivel do prof:"))
aulas_por_semana= int(input("insira quantas aulas por semana:"))
if nivel==1:
    valor_hora=12.00
elif nivel ==2:
    valor_hora=17.00
elif nivel==3:
    valor_hora=25.00
else:
    print("nivel invalido")
salario=aulas_por_semana*valor_hora

print(f"salario do professor é {salario}")