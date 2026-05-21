import os
os.system("cls")   

def exibir_menu():
    print("1- (Dollar - Real)")
    print("2- (Real - Dollar)")
    print("3- (Sair)")

def converter_real_para_dollar(qtd_real, tax_dollar):
    total_dollar=qtd_real/tax_dollar
    return total_dollar
def converter_dollar_para_real(qtd_dollar, tax_real):
    total_real=qtd_dollar*tax_real
    return total_real
def sair():
    input("obrigado por utilizar o programa, pressione <enter> para sair.")
    exit()
while True:
    os.system("cls")
    print("seja bem-Vindo(a) ao convensor de moedar!")

    exibir_menu()

    escolha = int(input("escolha uma das opções acima: "))

    if(escolha==1):
        os.system("cls")
        print("conversão de reais para dollar: ")
        
        qtd_real= float(input("informe a quantia em Reais que pretende converter para o Dollar: "))
        tax_dollar= float(input("informe a cotação do dollar: "))
        total_dollar=converter_real_para_dollar(qtd_real, tax_dollar)

        print(f"o total de dollares convertidos é de: {total_dollar}")

        input("pressione <enter> para prosseguir")

    elif(escolha==2):
        os.system("cls")
        print("conversão de dollar para Real: ")

        qtd_dollar=float(input("informe a quantia de dollar: "))
        tax_real=float(input("informe a cotação do real: "))
        total_real=converter_dollar_para_real(qtd_dollar, tax_real)

        print(f"o total de Reais convertidos é de: {total_real}")

        input("pressione <enter> para continuar")

    elif(escolha==3):
        sair()