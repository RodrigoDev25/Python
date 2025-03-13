# Importa a biblioteca requests, que facilita o envio de requisições HTTP para websites
import requests  
# Importa a biblioteca BeautifulSoup, que ajuda a fazer o parsing de documentos HTML
import bs4  
# Importa a biblioteca csv, que permite trabalhar com arquivos CSV (Comma Separated Values)
import csv  

# Define a URL do site que será acessado
url = "https://globo.com"  

# Realiza uma requisição HTTP para o site utilizando o método 'get' da biblioteca 'requests'
# O método 'get' retorna a resposta da requisição, que será armazenada na variável 'resposta'
resposta = requests.get(url)  

# Usa o BeautifulSoup para analisar o conteúdo HTML da resposta da requisição
# O parâmetro 'html.parser' indica que será usado o parser padrão do Python para ler o HTML
html = bs4.BeautifulSoup(resposta.text, "html.parser")  

# Encontra todos os elementos <h2> no HTML que possuem a classe 'post__title'
# O método 'find_all' retorna uma lista de todos os elementos que atendem ao critério de busca
# Nesse caso, estamos buscando os títulos dos posts no site
titulos = html.find_all("h2", class_="post__title")  

# Abre (ou cria, caso não exista) o arquivo CSV chamado 'lista-de-titulos.csv' em modo escrita ('w')
# O parâmetro 'encoding="utf-8"' garante que todos os caracteres (incluindo especiais) sejam corretamente salvos no arquivo
# O parâmetro 'newline=""' evita que quebras de linha extras sejam inseridas no arquivo, o que pode acontecer dependendo da plataforma
with open("lista-de-titulos.csv", "w", encoding="utf-8", newline="") as arquivo_csv:  
    # Cria um objeto 'escrever_csv' que permitirá escrever no arquivo CSV
    # 'csv.writer' é um objeto que facilita a escrita no formato CSV
    escrever_csv = csv.writer(arquivo_csv)  

    # Para cada 'titulo' na lista 'titulos' (que contém todos os títulos encontrados no HTML)
    for titulo in titulos:  
        # Escreve uma linha no arquivo CSV com o texto do título
        # 'titulo.get_text()' extrai apenas o texto contido no elemento <h2> (sem tags HTML)
        escrever_csv.writerow([titulo.get_text()])  

# Imprime uma mensagem informando que o arquivo CSV foi criado com sucesso
print("ARQUIVO CRIADO COM SUCESSO!")  
