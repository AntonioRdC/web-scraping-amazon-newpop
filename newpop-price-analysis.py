'''
    Utilizando o URL:'https://www.amazon.com.br/b?ie=UTF8&node=17202662011' do site Amazon. O programa
requisita o HTML do site e então é armazenado o 'NOME, AUTOR E PREÇO' dos livros contidos no site e enviados
para o usuario.
'''

import requests
from bs4 import BeautifulSoup

print('Executando...\n\n\n\n')


#Dicionario com os dados dos livros.
dados = {'Nome' : [], 'Autor' : [], 'Preço' : []}
#Requisitando o HTML do site com os dados dos livros.
html = BeautifulSoup(requests.get('https://www.amazon.com.br/b?ie=UTF8&node=17202662011').text, 'html.parser')


#Armazenando os Preços, Nomes e Autores dos livros pelo HTML.
for arquivo in html.select('.acs-product-block--default'):
    for i, nomeAutor in enumerate(arquivo.select('.a-truncate-full')):
        if i == 0:
            dados['Nome'] += nomeAutor
        else:
            dados['Autor'] += nomeAutor
    
    if arquivo.select_one('.a-offscreen') == None:
        dados['Preço'] += 'N'
    else:
        dados['Preço'] += arquivo.select_one('.a-offscreen')

for i, dado in enumerate(dados['Autor']):
    dados['Autor'][i] = dado.strip()

for i in range(0, 87):
    print(f"Nome: {dados['Nome'][i]}\nAutor: {dados['Autor'][i]}\nPreço: {dados['Preço'][i]}\n")

a = input('')