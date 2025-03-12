import csv  # Importa a biblioteca CSV para manipulação de arquivos CSV

# Abre o arquivo de texto contendo os emails no modo leitura ("r")
# "encoding='utf-8'" garante que caracteres especiais sejam lidos corretamente
arquivo_txt_com_emails = open("emails_aleatorios.txt", "r", encoding="utf-8") 

# Abre um novo arquivo CSV no modo escrita ("w")
# "newline=''" evita linhas em branco extras no CSV
arquivo_csv = open("lista-de-emails.csv", "w", newline="", encoding="utf-8")

# Lê todas as linhas do arquivo TXT, armazenando os emails em uma lista
emails = arquivo_txt_com_emails.readlines()

# Cria um objeto escritor para manipular o arquivo CSV
escritor_csv = csv.writer(arquivo_csv)

# Escreve o cabeçalho do arquivo CSV (nome da coluna)
escritor_csv.writerow(["Nomes"])

# Percorre a lista de emails e escreve cada email no arquivo CSV
for email in emails:
    escritor_csv.writerow([email.strip()])

# Fecha os arquivos para liberar memória
arquivo_txt_com_emails.close()
arquivo_csv.close()

# Mensagem de sucesso para o usuário
print("Arquivo 'lista-de-emails.csv' criado com sucesso!")