import os
os.system("cls")

ano=int(input("ano em que estamos:"))

if(ano % 4 ==0 and ano % 100!=0) or (ano % 400==0):
    print("ano bissexto")
else:
    print("não é ano bissexto")