import os
os.system("cls")
cotaçao=float(input("insira a cotação do dollar atual:"))
dollar=float(input("insira a quantia em dollar:"))
reais=dollar*cotaçao
print(f"na conversão fica {reais}RS")