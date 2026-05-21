import os
os.system("cls")

saldo = 1000

while True:
    print(f"seu saldo total é de {saldo}R$")

    print("1 → Ver saldo")
    print("2 → Depositar")
    print("3 → Sacar")
    print("4 → Sair")
    escolha=int(input("faça sua escolha: "))

    if escolha == 1:
        print(f"seu saldo atual é de {saldo}R$")
    elif escolha==2:
        valor_deposito = float(input("digite o valor que deseja depositar: "))
        saldo += valor_deposito
        print(f"seu saldo atual é de {saldo}R$")
    elif escolha==3:
        valor_saque = float(input("digite o valor que deseja sacar: "))
        if valor_saque > saldo:
            print("saldo insuficiente")
            break
        else:
         saldo -= valor_saque
         print(f"seu saldo atual é de {saldo}R$")
    elif escolha==4:
        print("você acaba de sair do caixa eletronico")
        break
    else:
        print("escolha invalida, porfavor reinicie e tente novamente")

