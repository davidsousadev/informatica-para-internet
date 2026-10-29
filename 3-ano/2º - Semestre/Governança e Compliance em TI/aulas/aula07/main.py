senhaapp = "wvaz tmbx pwzg tqhc"
# ~/Android/Sdk/emulator/emulator -avd Medium_Phone
from davidsousa import enviar_email
import bcrypt, random, string

# Passo 01 = Usuario e senha
usuarios = {}
usuarios[1] = {
    "nome": "David Sousa",
    "email": "davidffsousaff@gmail.com"
}

# Passo 02 = Proteger a senha
usuarios[1]["senha"] = input("Crie uma senha: ").strip()
usuarios[1]["senha"] = bcrypt.hashpw(usuarios[1]["senha"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

# Passo - Login
tentativas_login = 0
while tentativas_login < 3:
    login_email = input("Digite seu e-mail: ").strip()
    login_senha = input("Digite sua senha: ").strip()
    if login_email == usuarios[1]["email"] and (bcrypt.checkpw(login_senha.encode("utf-8"), usuarios[1]["senha"].encode("utf-8"))) == True:
        print("Login correto!")
        break
    else:
        print("E-mail ou senha incorretos!")
        tentativas_login += 1

# Passo 03 = Gerar codigo de 6 digitos
area51 = ''.join(
    random.choices(
        string.ascii_letters + string.digits, k=6
    )
)
nome_remetente = "David Sousa"
remetente = "davidk1k3k@gmail.com"
senha = senhaapp
destinatario = usuarios[1]["email"]
assunto = "Código de verificação"
corpo = area51
enviar_email(nome_remetente, remetente, senha, destinatario, assunto, corpo, importante=True, html=True)

# Passo 04 = 3 chances
tentativas = 3
while tentativas > 0:
    resposta = input("Digite o codigo de verificação: ").strip()
    if resposta == area51:
        print("Acesso Libarado!")
        break
    else:
        print("Codigo invalido!")
        tentativas -= 1
        if tentativas == 0:
            print("Acesso Bloqueado!")