import os
os.system("cls")

print("seja bem vindo ao boltim virtual!")

nota01= float(input("entre com a primeira nota:"))
nota02= float(input("entre com a segunda nota:"))
nota03= float(input("entre com a terceira nota:"))

media= nota01+nota02+nota03/3

if (media>=6):
    print("aprovado!")
elif (media >=4 and media <= 5):
    print("recuperação")
else:
    print("reprovado")
  

print (f"sua media foi {media}")