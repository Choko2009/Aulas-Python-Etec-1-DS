
import os

Filmes = [
    {
        "titulo": "O Poderoso Chefão",
        "genero": "Crime",
        "ano": 1972,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Interestelar",
        "genero": "Ficção Científica",
        "ano": 2014,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Cidade de Deus",
        "genero": "Drama",
        "ano": 2002,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Matrix",
        "genero": "Ação",
        "ano": 1999,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Titanic",
        "genero": "Romance",
        "ano": 1997,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Avatar",
        "genero": "Ficção Científica",
        "ano": 2009,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Vingadores: Ultimato",
        "genero": "Ação",
        "ano": 2019,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Clube da Luta",
        "genero": "Drama",
        "ano": 1999,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Forrest Gump",
        "genero": "Drama",
        "ano": 1994,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
    {
        "titulo": "Gladiador",
        "genero": "Ação",
        "ano": 2000,
        "avaliações": [],
        "media": 0,
        "classificacao": "Sem classificação",
        "disponivel": True,
        "cliente": None,
    },
]


def exibir_catalogo(Filmes):
    os.system("cls")
    print("Catálogo de Filmes:\n")

    for item in Filmes:
        print(f"Título - {item['titulo']}")
        print(f"Ano de Lançamento - {item['ano']}")
        print(f"Gênero - {item['genero']}")
        print(f"Avaliação - {round(item['media'], 1)}")
        print(f"Classificação - {item['classificacao']}")

        if item['disponivel'] == True:
            status = "Disponível para alugar"
        else:
            status = f"Alugado pelo cliente {item['cliente']}"

        print(f"Status - {status}")
        print("-" * 40)


def alugar_filme(Filmes):
    os.system("cls")
    print("===ALUGUEL DE FILME===")
    titulo = input("Digite o nome do filme: ")

    for item in Filmes:
        if item['titulo'].lower() == titulo.lower():

            if item['disponivel'] == True:
                nome = input("Insira seu nome: ")
                item['disponivel'] = False
                item['cliente'] = nome
                input("Filme alugado com sucesso! Pressione <enter> para continuar.")
            else:
                input(f"Filme alugado pelo cliente {item['cliente']}")
                input("Pressione <enter> para continuar.")
            return

    input("Filme não encontrado.")


def calcular_media(avaliações):

    media = sum(avaliações) / len(avaliações)

    if media >= 9:
        return "Absolute Cinema(Excelente)"
    elif media >= 7:
        return "Bom"
    elif media >= 5:
        return "Regular"
    else:
        return "Flopado(RUIM)"


def melhor_filme(Filmes):
    return max(Filmes, key=lambda x: x['media'])


def pior_filme(Filmes):
    return min(Filmes, key=lambda x: x['media'])


def devolver_filme(Filmes):

    os.system("cls")
    print("===DEVOLUÇÃO DE FILME===")

    titulo = input("Digite o nome do filme para devolver: ")

    for item in Filmes:

        if item['titulo'].lower() == titulo.lower():

            if item['disponivel'] == False:

                print(f"Filme estava com o cliente {item['cliente']}")

                nota = float(input("Avalie o filme de 0 a 10: "))

                item['avaliações'].append(nota)

                item['media'] = (
                    sum(item['avaliações']) / len(item['avaliações'])
                )

                item['classificacao'] = calcular_media(item['avaliações'])

                item['disponivel'] = True
                item['cliente'] = None

                input("Filme devolvido com sucesso! Pressione <enter> para continuar.")

            else:
                input("Esse filme já está disponível. Pressione <enter> para continuar.")

            return

    input("Filme não encontrado. Pressione <enter> para continuar.")


def carregar_menu_cliente(Filmes):
    os.system("cls")

    while True:
        os.system("cls")

        print("=== MENU DO CLIENTE ===")
        print("[1] - Ver Catálogo")
        print("[2] - Alugar Filme")
        print("[3] - Devolver Filme")
        print("[4] - Voltar")

        op = int(input("Escolha uma opção: "))

        if op == 1:
            exibir_catalogo(Filmes)
            input("Pressione <enter> para continuar.")

        elif op == 2:
            alugar_filme(Filmes)

        elif op == 3:
            devolver_filme(Filmes)

        elif op == 4:
            break

        else:
            input("Opção inválida.")


def carregar_menu_admin(Filmes):

    os.system("cls")
    print("=== AUTENTICAÇÃO DE ADMINISTRADOR ===")

    usuario = input("Insira seu nome de usuário: ")
    senha = input("Insira sua senha: ")

    if usuario != "admin" or senha != "123":
        input("Acesso negado | Pressione <enter> para tentar novamente.")
        return

    while True:

        os.system("cls")

        print("Bem-vindo(a), administrador!")
        print("[1] - Cadastrar Filme")
        print("[2] - Lista de Filmes")
        print("[3] - Top e Flops")
        print("[4] - Voltar")

        op = int(input("Escolha uma opção: "))

        if op == 1:

            os.system("cls")
            print("=== CADASTRANDO FILME ===")

            titulo = input("Digite o título do filme: ")
            genero = input("Digite o gênero do filme: ")
            ano = int(input("Digite o ano de lançamento do filme: "))

            filme = {
                "titulo": titulo,
                "genero": genero,
                "ano": ano,
                "avaliações": [],
                "media": 0,
                "classificacao": "Sem classificação",
                "disponivel": True,
                "cliente": None,
            }

            Filmes.append(filme)

            input("Filme cadastrado com sucesso!")

        elif op == 2:

            exibir_catalogo(Filmes)
            input("Pressione <enter> para voltar ao menu.")

        elif op == 3:

            os.system("cls")
            print("Top e Flops...")

            melhor = melhor_filme(Filmes)
            pior = pior_filme(Filmes)

            print(
                f"Melhor filme: {melhor['titulo']} - Avaliação: {round(melhor['media'],1)} - Classificação: {melhor['classificacao']}"
            )

            print(
                f"Pior filme: {pior['titulo']} - Avaliação: {round(pior['media'],1)} - Classificação: {pior['classificacao']}"
            )

            input("Pressione <enter> para continuar.")

        elif op == 4:
            break

        else:
            input("Opção inválida. Pressione <enter> para tentar novamente.")


while True:

    os.system("cls")

    print("=== LOCADORA DE FILMES ===")
    print("[1] - Entrar como Cliente")
    print("[2] - Entrar como Administrador")
    print("[3] - Sair")

    op = int(input("Escolha uma opção: "))

    if op == 1:

        carregar_menu_cliente(Filmes)

    elif op == 2:

        carregar_menu_admin(Filmes)

    elif op == 3:

        input("Obrigado por usar a Locadora | Pressione <enter> para sair.")
        break

    else:

        input("Opção inválida. Tente novamente.")