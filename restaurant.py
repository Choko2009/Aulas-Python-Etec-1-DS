import os
os.system("cls")
def mostrar_menu():
    print("=" * 50)
    print("RESTAURANTE")
    print("1 - Dinheiro")
    print("2 - VR")
    print("3 - Cartão")
    print("=" * 50)
def calcular_taxa(valor_compra, escolha):
    if escolha == "1":
        forma_pagamento = "DINHEIRO"
        taxa_pagamento = 0
    elif escolha == "2":
        forma_pagamento = "VR"
        taxa_pagamento = valor_compra * 0.02
    elif escolha == "3":
        forma_pagamento = "CARTÃO"
        taxa_pagamento = valor_compra * 0.03
    else:
        print("Opção inválida!")
        exit()
    return forma_pagamento, taxa_pagamento
mostrar_menu()
escolha = input("Insira aqui a forma de pagamento: ")
qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
valor_compra = float(input("Entre com o valor total da compra: "))
forma_pagamento, taxa_pagamento = calcular_taxa(valor_compra, escolha)
valor_com_taxa = valor_compra + taxa_pagamento
taxa_garcom = valor_com_taxa * 0.10
valor_final = valor_com_taxa + taxa_garcom
valor_pessoa = valor_final / qtd_pessoas
input("Pressione ENTER para ver o resultado...")
os.system("cls")
print("=" * 50)
print(f"A forma de pagamento escolhida foi em: {forma_pagamento}")
print(f"Valor original da sua compra foi de: R$ {valor_compra:.2f}")
print(f"Valor da taxa de pagamento: R$ {taxa_pagamento:.2f}")
print(f"Valor do garçom: R$ {taxa_garcom:.2f}")
print(f"Valor total: R$ {valor_final:.2f}")
print(f"Quanto cada pessoa deverá pagar: R$ {valor_pessoa:.2f}")
print("=" * 50)



