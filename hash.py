import hashlib

#HASH DO TIPO SHA256
h = hashlib.sha256()

senha = input('Digite a senha: ')

#PEGA A STRING E TRANSFORMA EM BYTES
bt = bytes(senha, encoding="utf-8")

#PEGA OS BYTES E TRANSFORMA EM HASH
h.update(bt)

#ARMAZENA A HASH
btHash = h.hexdigest()
print(btHash)

nSenha = input('Digite a senha: ')
newSenhaBt = bytes(nSenha, encoding="utf-8")

s = hashlib.sha256()
s.update(newSenhaBt)

nSenha = s.hexdigest()
print(nSenha)

if nSenha == btHash:
    print('OK')

else:
    print('EEROOO')