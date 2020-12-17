import hashlib

#HASH DO TIPO SHA256
h = hashlib.sha256()

senha = input('Digite a senha: ')

#PEGA A STRING E TRANSFORMA EM BYTES
bt = bytes(senha, encoding="utf-8")

#PEGA OS BYTES E TRANSFORMA EM HASH
h.update(bt)

nSenha = input('Digite a senha: ')
newSenhaBt = bytes(nSenha, encoding="utf-8")

if newSenhaBt == bt:
    print('OK')

else:
    print('EEROOO')