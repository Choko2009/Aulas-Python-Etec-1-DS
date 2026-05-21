import os

os.system("cls")

resposta = "sim"

while True:
    os.system("cls")

    print("=== menu ===")
    print("[1] calcular o salario")
    print("[2] sair do programa")

    opcao = int(input("escolha una opção:"))

   #verificando  qual foi a opçao escolhida
   if(opcao == 1):

        print("qual o nivel do professor")
        print("[1] - nivel 1")
        print("[2] - nivel 2")
        print("[3] - nivel 3")
     



        nivel = int(input("escolha um nivel:"))

        if (nivel>=4):
            print("nivel invalido")
            input("precione <enter> para contnuar....")
            continue

        else:
            qtd_aulas = int(input("informe a qtd de aulas mensais:"))

        if(nivel == 1):
            salario = qtd_aulas * 12
        elif(nivel == 2):
            slario = qtd_aulas * 17
        elif(nivel == 3):
            slario = qtd_aulas * 25
        else:
            print("nivel invalido")
            input("precione <enter> para continuar....")
            continue
            print(f"o salario do professo será: {salario}")
        resposta = input("gostaria de execultar novamente?:(sim ou não)")


        input("Preciomne <enter> para continuar...")

elif(opcao == 2):
    input("pressione enter pra encerrar o programa...")
    break

print("finalizou o programa")'