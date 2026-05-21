peso = float(input("entre com seu peso:"))
import os
os.system("cls")

altura = float(input("entre com sua altura:"))
imc = peso / (altura**2)
print(f"seu IMC é: {imc}")
if imc < 16.9:
    print("muito abaixo do peso")
elif imc <= 18.4:
    print("abaixo do peso")
elif imc <= 29.9:
    print("acima do peso")
elif imc <= 34.9:
    print("obesidade grau I")
elif imc<=40:
    print("obesidade grau II")
else:
    print("obesidade grau III")