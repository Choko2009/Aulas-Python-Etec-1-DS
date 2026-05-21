import os
os.system("cls")
estoque= int(input("entre com a quantidade de estoque:"))
if estoque<5:
    print("estoque abaixo")
elif estoque>=5:
    print("estoque OK")