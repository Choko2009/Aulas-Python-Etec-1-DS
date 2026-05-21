import os
os.system("cls")

num0= float(input("entre com o primeiro numero:"))
num1=float(input("entre com o segundo numero:"))
print("escolha uma das opçoes abaixo")
print ("+ - adição")
print ("- - subtração")
print ("* - multiplicação")
print ("/ - divisão")
operação= input("informe a operação que deseja usar:")

if (operação == "+"):
    resultado=num0+num1
elif(operação=="-"):
    resultado=num0-num1
elif(operação=="*"):
    resultado=num0*num1
elif(operação=="/"):
    resultado=num0/num1
else:
   print ("operaçao invalidada")
print("="*50)
print(f"resultado de {num0}{operação}{num1} é igual à {resultado}")