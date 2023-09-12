import re

cpf = '111.111.111.111'
padrao = re.compile('[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}')

print(re.fullmatch(padrao, cpf))

