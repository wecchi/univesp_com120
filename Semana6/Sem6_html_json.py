## Programação orientada para WEB
import json
d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
# Convertendo o dicionário num formato JSON
jd = json.dumps(d)
print(jd)
# Lendo um formato JSON
dd = json.loads(jd)
print(dd)


## Processamento de elementos WEB - acesso a 
"""
    O módulo urllib.request permite requisitar e receber recursos da Web, de modo similar a um navegador.
    A função urlopen():
        -recebe como parâmetro uma URL
        -formula uma requisição HTTP que será enviada ao servidor especificado na URL
        -obtém e retorna uma resposta HTTP completa do servidor.
"""
from urllib.request import urlopen

def getSource(url):
    # Faz a chamada a url
    response = urlopen(url)
    # Lê o conteúdo no formato HTML
    html = response.read()
    # Decodifica em elementos HTML
    return html.decode()


html = getSource('https://www.tecmundo.com.br/mercado/133755-cursos-online-aprender-data-science-inteligencia-artificial.htm')
print(html)

infile = open('webscraping.txt', 'w')
infile.write(html)
infile.flush()
print('''Arquivo "{}" criado com sucesso!'''.format('webscraping.txt'))

## Módulo HTML Parser
"""
    O módulo html.parser, por meio da classe HTMLParser, permite processar elementos HTML de uma página Web.
    O método feed() da classe HTMLParser recebe como entrada uma página HTML no formato string,
    e para cada 'token' lido (tags de início, tags de fim, texto, etc.), executa um handler correspondente.
    
    Para trazer funcionalidade a um determinado handler, precisamos sobrescrever o método correspondente, 
    estendendo a classe HTMLParser.
"""
from html.parser import HTMLParser

class dsParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        """
        estendendo funcionalidade para um elemento, sobrescrevendo o método correspondente
        :param tag:
        :param attrs:
        :return:
        """
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    #imprimir todos os links existentes no html
                    print(attr[1])


# Lê o arquivo gravado anteriormente (backup dos dados)
infile = open('webscraping.txt', 'r')
content = infile.read()
infile.close()


parser = dsParser()
parser.feed(content)

## Retornar o número de polos de um determinado curso da UNIVESP.
from html.parser import HTMLParser
from urllib.request import urlopen, Request

class MyParser(HTMLParser):
    # Ao iniciar a classe estende o HTMLParser com o atributo n_polos
    def __init__(self):
        HTMLParser.__init__(self)
        self.n_polos = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'item-polos':
                    self.n_polos += 1

    def num_polos(self):
        return self.n_polos


def getSource(url):
    # Criando uma requisição simulando como se estivesse sendo feito via um navegador
    # web - alguns servidores não respondem a webscraping
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    # reg_url = "https:XXXXOOOO"
    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    return html.decode()


url = 'https://univesp.br/cursos/engenharia-de-computacao'
html = getSource(url)
parser = MyParser()
parser.feed(html)
parser.num_polos()