from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re  # Importe o módulo re

# O webscraping, também conhecido como raspagem de dados da web, é uma técnica utilizada para extrair informações de páginas da internet.
# Selenium - literalmente abre um googleChrome para buscar as coisa que queremos
# Service é usado apra abrir uma instância do Chome WebDriver
service =  Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


# Manipular a instância os dados 

url = 'https://books.toscrape.com/'
driver.get(url)
html_page = driver.page_source
#print(html_page)

# 01 - Título de todos os livros da Página. 
regex_titulo = r'<h3><a .*? title="(.*?)">'
match_titulo = re.findall(regex_titulo, html_page, re.DOTALL)

print('01 - Título de todos os livros da Página. \n')
for titulo in match_titulo:
    print(titulo)
print('____________________________________________________________________________________\n')

# Tokenização é basicamente converter um texto em uma lista de palavras ou símbolos. 
# O processo de tokenização divide o título em palavras individuais.
# 02 - Tokenização aplicado nos títulos dos livros e caracteres convertidos pra minúsculas.
regex_token_titulo = r'<h3><a .*? title="(.*?)">'
match_token_titulo = re.findall(regex_token_titulo, html_page, re.DOTALL)

print('02 - Tokenização aplicado nos títulos dos livros e caracteres convertidos pra minúsculas: \n')
for token in match_token_titulo:
    tokenizacao = token.lower()
    tokenizacao = tokenizacao.replace(' ', '\n')
    print(tokenizacao)
print('____________________________________________________________________________________\n')

# 03 - Preço dos livros da Página. 
regex_preco_livro = r'£(\d+\.\d{2})'
match_preco_livro = re.findall(regex_preco_livro, html_page, re.DOTALL)

print('03 - Preço dos livros da Página: \n')
for preco_livro in match_preco_livro:
    print(preco_livro)
print('____________________________________________________________________________________\n')

# 04 - Limpeza Substituição de ponto por vírgula nos preços dos livros da página:
regex_preco_livro = r'£(\d+\.\d{2})'
match_preco_livro = re.findall(regex_preco_livro, html_page, re.DOTALL)
print('04 - Limpeza Substituição de ponto por vírgula nos preços dos livros da página: \n')
for preco in match_preco_livro:
    preco_modificado = preco.replace('.', ',')
    print(preco_modificado)
print('____________________________________________________________________________________\n')
      
# 05 - Livros com preço de até 20 libras.
regex_preco_20_libras = r'£(0(\.\d{2})?|1\d\.\d{2}|20\.00)'
match_preco_20_libras = re.findall(regex_preco_20_libras, html_page, re.DOTALL)

print('05 - Livros com preço de até 20 libras: \n')
for preco_20_libras in match_preco_20_libras:
    if isinstance(preco_20_libras, tuple):
        print(''.join(preco_20_libras))
    else:
        print(preco_20_libras)
print('____________________________________________________________________________________\n')

# 06 - Busca Todos os Títulos do Menu.
regex_menu = r'<a href="catalogue/category/books/[^/]+/index\.html">\s*([^<\s].*?)\s*</a>'
match_menu = re.findall(regex_menu, html_page, re.DOTALL)

print('Busca 06 - Todos os Títulos do Menu: \n')
for menu in match_menu:
        print(menu)
print('____________________________________________________________________________________\n')


# Tokenização é basicamente converter um texto em uma lista de palavras ou símbolos. 
# O processo de tokenização divide o título em palavras individuais.
# 07 - Tokenização aplicado nos títulos do menu.
regex_menu_token = r'<a href="catalogue/category/books/[^/]+/index\.html">\s*([^<\s].*?)\s*</a>'
match_menu_token = re.findall(regex_menu_token, html_page, re.DOTALL)

print('07 - Tokenização aplicado nos títulos do menu: \n')
for menu_token in match_menu_token:
    tokenizacao_menu = menu_token.upper()
    tokenizacao_menu = tokenizacao_menu.replace(' ', '\n')
    print(tokenizacao_menu)
print('____________________________________________________________________________________\n')



time.sleep(1000)

# Fecha o navegador
driver.quit()
