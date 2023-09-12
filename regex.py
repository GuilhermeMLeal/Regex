# Expressao regular serve para definir um determinado padrão de String e buscar ou  verificar se uma string está naquele determinado padrão

#Padrão e buscá-lo em outras Strings

import re

String_default= 'hp'
# Compile cria um padrão
pattern = re.compile("[^h]") # tudo aquilo que é diferente da letra h

print(re.findall(pattern,String_default))

#print(re.fullmatch(default,String_default)) # Reconhece o padrão de uma string inteira e compara
#print(re.search(default, String_default)) # busca somente a primeira vez que aquele caracter aparece'
#print(re.findall(default, String_default)) # busca todos os conjuntos de caracteres que atendem aquele padrao



# . representa qualquer caracter menos \n, qualquer coisa
# \. representa que uma String finaliza o padrão com um ponto
# [] Conjunto serve para a gente isolar conjuntos de operações
# ^ representa o inicio de um caracter
# $ representa o final dea uma String
# [^] String diferente do que está dentro de um conjunto

String_default= 'hp.@123'

pattern = re.compile("[\w]") 
pattern = re.compile("^[\W]") 
pattern = re.compile("[\W]") 

# w caracter alfa numerico
# W nao é um caracter alfa numerico (.,"")

# \d numeros de 0 a 9
# \D not in 0 a 9

String_default= '123.m '

pattern2 = re.compile("[\w\s]")  #conjunto de possibilidades


print(re.findall(pattern2,String_default))

# \s caracter vazio
# \S nao vazio

String_default2 = 'Guilherme Diniz Fernandes12'

pattern3  = re.compile("^[a-zA-Z0-9]")
print(re.findall(pattern3,String_default2))


String_default3 = "Guilherme Martins"
pattern4  = re.compile("[a-zA-Z0-1]+")
print(re.fullmatch(pattern4,String_default3))

# + infinitas possibilidades
# * 0 a infinitas 
# ? de 0 a 1 possibilidade

String_default3 = "Guilherme"
pattern4  = re.compile("[a-zA-Z0-1]{8,10}")
print(re.fullmatch(pattern4,String_default3))