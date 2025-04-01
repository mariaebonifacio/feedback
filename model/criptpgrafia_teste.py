from hashlib import sha256

senha = "teste"
# criptografando a senha
senha_criptografada = sha256(senha.encode()).hexdigest()

print(senha_criptografada)

