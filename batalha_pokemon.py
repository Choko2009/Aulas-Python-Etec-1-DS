import os
os.system("cls")
import time
import random

nome = input("Insira o nome do Treinador: ")

HP_player = 20
HP_bot = 20

print("1 - Charmander")
print("2 - Squirtle")
print("3 - Bulbasaur")

escolha = input("Escolha seu Pokémon: ")

if escolha == "1":
    pokemon_player = "Charmander"
    pokemon_tipo = "Fogo"
elif escolha == "2":
    pokemon_player = "Squirtle"
    pokemon_tipo = "Água"
elif escolha == "3":
    pokemon_player = "Bulbasaur"
    pokemon_tipo = "Planta"
else:
    print("Escolha inválida")
    exit()

escolha_bot = random.randint(1, 3)

if escolha_bot == 1:
    pokemon_bot = "Charmander"
    poke_tipo_bot = "Fogo"
elif escolha_bot == 2:
    pokemon_bot = "Squirtle"
    poke_tipo_bot = "Água"
else:
    pokemon_bot = "Bulbasaur"
    poke_tipo_bot = "Planta"

time.sleep(1)
print(f"O treinador {nome} escolheu {pokemon_player} ({pokemon_tipo})")
time.sleep(1)
print(f"O inimigo escolheu {pokemon_bot} ({poke_tipo_bot})")

time.sleep(1)
print("BATALHA INICIADA!!")

while HP_player > 0 and HP_bot > 0:

    Golpe_bot = random.randint(1, 4)

    if pokemon_bot == "Charmander":
        if Golpe_bot == 1:
            dano_bot = 5
            nome_ataque_bot = "Scratch"
        elif Golpe_bot == 2:
            dano_bot = 2
            nome_ataque_bot = "Growl"
        elif Golpe_bot == 3:
            dano_bot = 10
            nome_ataque_bot = "Flamethrower"
        elif Golpe_bot == 4:
            dano_bot = 7
            nome_ataque_bot = "Ember"

    elif pokemon_bot == "Bulbasaur":
        if Golpe_bot == 1:
            dano_bot = 4
            nome_ataque_bot = "Tackle"
        elif Golpe_bot == 2:
            dano_bot = 5
            nome_ataque_bot = "Vine Whip"
        elif Golpe_bot == 3:
            dano_bot = 6
            nome_ataque_bot = "Razor Leaf"
        elif Golpe_bot == 4:
            dano_bot = 9
            nome_ataque_bot = "Solar Beam"

    elif pokemon_bot == "Squirtle":
        if Golpe_bot == 1:
            dano_bot = 3
            nome_ataque_bot = "Tail Whip"
        elif Golpe_bot == 2:
            dano_bot = 4
            nome_ataque_bot = "Water Pulse"
        elif Golpe_bot == 3:
            dano_bot = 5
            nome_ataque_bot = "Tackle"
        elif Golpe_bot == 4:
            dano_bot = 7
            nome_ataque_bot = "Water Gun"

    if pokemon_player == "Charmander":
        print("Ataques do Charmander:")
        print("1 - Scratch (-5 HP)")
        print("2 - Growl (-2 HP)")
        print("3 - Flamethrower (-10 HP)")
        print("4 - Ember (-7 HP)")

        ataque = input("escolha: ")

        if ataque == "1":
            dano = 5
            nome_ataque = "Scratch"
        elif ataque == "2":
            dano = 2
            nome_ataque = "Growl"
        elif ataque == "3":
            dano = 10
            nome_ataque = "Flamethrower"
        elif ataque == "4":
            dano = 7
            nome_ataque = "Ember"
        else:
            print("Ataque inválido!")
            dano = 0
            nome_ataque = "Nada"

    elif pokemon_player == "Bulbasaur":
        print("Ataques do Bulbasaur:")
        print("1 - Tackle (-4 HP)")
        print("2 - Vine Whip (-5 HP)")
        print("3 - Razor Leaf (-6 HP)")
        print("4 - Solar Beam (-9 HP)")

        ataque = input("escolha: ")

        if ataque == "1":
            dano = 4
            nome_ataque = "Tackle"
        elif ataque == "2":
            dano = 5
            nome_ataque = "Vine Whip"
        elif ataque == "3":
            dano = 6
            nome_ataque = "Razor Leaf"
        elif ataque == "4":
            dano = 9
            nome_ataque = "Solar Beam"
        else:
            print("Ataque inválido!")
            dano = 0
            nome_ataque = "Nada"

    elif pokemon_player == "Squirtle":
        print("Ataques do Squirtle:")
        print("1 - Tail Whip (-3 HP)")
        print("2 - Water Pulse (-4 HP)")
        print("3 - Tackle (-5 HP)")
        print("4 - Water Gun (-7 HP)")

        ataque = input("escolha: ")

        if ataque == "1":
            dano = 3
            nome_ataque = "Tail Whip"
        elif ataque == "2":
            dano = 4
            nome_ataque = "Water Pulse"
        elif ataque == "3":
            dano = 5
            nome_ataque = "Tackle"
        elif ataque == "4":
            dano = 7
            nome_ataque = "Water Gun"
        else:
            print("Ataque inválido!")
            dano = 0
            nome_ataque = "Nada"

    HP_bot -= dano
    if HP_bot < 0:
        HP_bot = 0

    print(f"{pokemon_player} usou {nome_ataque}!")
    print(f"Causou {dano} de dano em {pokemon_bot}")
    print(f"HP de {pokemon_bot}: {HP_bot}")

    if HP_bot <= 0:
        break

    HP_player -= dano_bot
    if HP_player < 0:
        HP_player = 0

    print(f"{pokemon_bot} usou {nome_ataque_bot}!")
    time.sleep(1)
    print(f"Causou {dano_bot} de dano em {pokemon_player}")
    time.sleep(1)
    print(f"HP de {pokemon_player}: {HP_player}")

if HP_bot <= 0:
    print(f"{pokemon_bot} foi derrotado!")
    print(f"{nome} venceu a batalha!")
else:
    print(f"{pokemon_player} foi derrotado!")
    print("Você perdeu!")