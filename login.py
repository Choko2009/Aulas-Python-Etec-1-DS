usuario = input("entre com seu nome: ")
senha = input("entre com sua senha: ")
usuario_admin="joão"
senha_admin="123"
if usuario == usuario_admin and senha == senha_admin:
    print("acesso permitido")
else:
    print("acesso negado")