def obter_valor_hora(tipo):
    if tipo == 1:
        return 5.0, "Moto"
    elif tipo == 2:
        return 8.0, "Carro"
    elif tipo == 3:
        return 12.0, "SUV"
    else:
        return 0, "Inválido"


def calcular_taxa(valor, horas):
    if horas > 10:
        return valor * 0.10
    elif horas > 5:
        return valor * 0.05
    else:
        return 0


def main():
    print("===== ESTACIONAMENTO =====")

    nome = input("Digite o nome do cliente: ")

    print("\nTipos de veículo:")
    print("[1] Moto")
    print("[2] Carro")
    print("[3] SUV")

    tipo = int(input("Digite o tipo do veículo: "))
    horas = float(input("Digite a quantidade de horas estacionado: "))

    valor_hora, descricao = obter_valor_hora(tipo)

    if valor_hora == 0:
        print("Tipo de veículo inválido!")
        return

    valor_sem_taxa = valor_hora * horas
    taxa = calcular_taxa(valor_sem_taxa, horas)
    valor_total = valor_sem_taxa + taxa
    valor_medio_hora = valor_total / horas

    print("\n===== RESUMO =====")
    print("Cliente:", nome)
    print("Tipo do veículo:", descricao)
    print("Quantidade de horas:", horas)
    print(f"Valor sem taxas: R$ {valor_sem_taxa:.2f}")
    print(f"Valor da taxa adicional: R$ {taxa:.2f}")
    print(f"Valor total final: R$ {valor_total:.2f}")
    print(f"Valor médio pago por hora: R$ {valor_medio_hora:.2f}")


main()