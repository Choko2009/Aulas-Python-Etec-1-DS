import os
os.system("cls")

semaforo= input("qual a cor do semaforo??")
pode = "verde"
atenção = "amarelo"
não_pode = "vermelho"
if semaforo == pode:
    print("pode falar")
elif semaforo == atenção:
    print("atenção")
elif semaforo== não_pode:
    print("pare")
else:
    print("cor invalida")