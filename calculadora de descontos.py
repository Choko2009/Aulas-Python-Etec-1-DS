import os
os.system('cls')

nome = input("nome do produto: ")
preco = float (input("preço do produto: "))
desconto = float (input ("qual o percentual do produto: "))
valor = preco*desconto / 100
final = preco - valor 
print("======================================================")
print (f"o preço original é de {preco}R$ - preço com desconto {final}")