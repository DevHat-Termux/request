!/usr/bin/python

# Importa o modulo request
import requests

# Pergunta a URL de qualquer site
x = input('URL:')

# Faz uma requisuçao get para a URL especificada
y = requests.get(x)

# Armazena na variavel z o cabeçalho da requisiçao
z = y.headers

#Cria um loop para percorrer os itens do cabeçalho HTTP
for a, b in z.items():

#Imprime o resultado do loop na tela
 print(f'{a} : {b}')
