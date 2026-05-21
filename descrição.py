import os
os.system("cls")

descrição = input("entre com a descrição do produto:")
quantidade = int(input("entre com a quantidade do produto:"))
preço_uni=float(input("entre com o preço por unidade:"))
total=quantidade*preço_uni
if quantidade<=5:
    desconto = total * 0.02
elif quantidade<=10:
    desconto = total * 0.03
else:
    desconto = total * 0.05
total_pagar=total-desconto
print(f"produto {descrição}")
print(f"total sem desconto {total}")
print(f"desconto {desconto}")
print(f"total a pagar {total_pagar}")