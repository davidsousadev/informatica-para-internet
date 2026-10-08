usuarios = {}



# import random
# import string
# from argon2 import PasswordHasher

# ph = PasswordHasher()

# usuarios = {}

# def adicionar_usuario():
#    nome = input("Nome: ")
#    email = input("E-mail: ")
#    senha = input("Senha: ")
#    hash_senha = ph.hash(senha)
#    usuarios[email] = {
#     "nome": nome,
#     "senha": hash_senha
# }

# def listar_usuarios():
#     for email in usuarios:
#         print(email)
#     print(usuarios[email]["nome"])

# def login():
#     email = input("E-mail: ")
#     senha = input("Senha: ")
#     if email not in usuarios:
#         print("Usuário não encontrado!")
#         return
#     ph.verify(
#     usuarios[email]["senha"],
#     senha)
#     if ph.verify(usuarios[email]["senha"], senha):
#         print("Senha correta!")