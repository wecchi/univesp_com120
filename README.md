# COM120 - Algoritmos e Programação de Computadores II

Composição de programas com múltiplos arquivos de código fonte, uso de bibliotecas, APIs (WEB) e GUIs. Noções de programação orientada a objetos. Depuração de programas. Testes automatizados.

Conceito e uso de pilhas, filas, listas, árvores. Recursão. Algoritmos de Ordenação e Busca.
Noções de gerenciamento de memória e manipulação de listas. Módulos e noções de objetos, arquivos. Modularização (módulos, bibliotecas, interfaces). Uso de APIs básicas da WEB e manipulação de dados (JSON). Criação de interfaces gráficas simples. Controle de Versão (GIT). 

## Exercícios práticos:

Relacionei alguns exercícios realizados no 4º bimestre/2020 durante as aulas da disciplina COM120 do Curso de Bacharel de Ciência de Dados da Univesp. Abaixo segue uma breve descrição do problema de negócios e da solução em Python (o link direciona para o código):

> Gerenciamento de memória, arquivos e depuração de programas
  1. [Extrair palavras de aquivo 1](Semana1/Aula02_Arquivos.py): leitura de um arquivo texto, imprime as palavras encontradas e retorna a quantidade de palavras e o tamanho do arquivo lido.
  2. [Contar ocorrências de palavra num arquivo](Semana1/ProblemaPratico_4_7.py): leitura de um arquivo texto para obter quantidade de ocorrências de uma palavra a ser localizada.
  3. [Extrair palavras de aquivo 2](Semana1/ProblemaPratico_4_8.py): leitura de um arquivo texto para obter quantidade de palavras (desconsiderando símbolos de pontuação) e impressão da lista de palavras.
  4. [Contar linhas contendo palavra específica](Semana1/ProblemaPratico_4_9.py): impressão das linhas de um arquivo que contenham pelo menos uma ocorrência de uma palavra a ser localizada.
  5. [Trocar primeiro com último item de uma lista](Semana1/ProblemaPratico_3.14.py): função trocaPU(), que aceita uma lista como entrada e troca a posição entre o primeiro e último elementos da lista
  6. [Desenhar do símbolo da olimpíada](Semana1/ProblemaPratico_3.15.py): função olimpíadas(t), que faz com que a tartaruga t desenhe os anéis olímpicos.
  7. [MDC - Obter Máximo Divisor Comum](Semana1/Sem1_textobase_cap3_p76.py): algoritmo para calcular o máximo divisor comum entre dois números
  8. [Calcular força exercida por um líquido](Semana1/Sem1_textobase_cap3_p81.py): função para calcular a força exercida na válvula de um reservatório cilíndrico contendo um líquido de peso específico conhecido.
  9. [Extrair raízes de uma equação do 2º grau](Semana1/Sem1_textobase_cap3_p87.py): algoritmo para calcluar raízes de uma equação de segundo grau (Ax² + Bx + C).
  10. [Gerar e ler arquivo texto](Semana1/Sem1_textoBase_ex7_1_p169.py): trechos de códigos para gravação e leitura de um arquivo texto
  11. [Gerar um arquivo com entrada de números reais 1](Semana1/Sem1_textoBase_ex7_1a_p173.py): programa que permaneça em laço lendo e gravando números reais em um arquivo até que seja digitado 0.
  12. [Ler e somar números de um arquivo 1](Semana1/Sem1_textoBase_ex7_2a_p174.py): programa que leia um arquivo texto contendo um número inteiro em cada linha, exiba na tela e faça a totalização dos valores lidos.
  13. [Gerar um arquivo com entrada de números reais 2](Semana1/Sem1_textoBase_ex7_1b_p173.py): programa que permaneça em laço lendo números reais até que seja digitado 0, gravando todos os números num arquivo a partir da lista de números criada.
  14. [Ler e somar números de um arquivo 2](Semana1/Sem1_textoBase_ex7_2b_p175.py): leitura de arquivo com totalização de valores – solução com iterador de arquivo.
  15. [Calcular média de temperaturas](Semana1/Sem1_textobase_cap3_p96.py): média de N temperaturas fornecidas pelo usuário
  16. [Imprimir lista de compras com totais](Semana1/Sem1_textoBase_ex7_3_p177.py): leitura de um arquivo texto que contém diversas linhas que representam uma lista de compras. Impressão da lista com totais.
  17. [Gerar inventário de estoque](Semana1/Sem1_textoBase_ex7_4_p178.py): programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas, simulando um inventário de estoque contendo código do produto, quantidade em estoque, valor unitário e ICMS a ser aplicado.
  18. [Processar inventário de estoque](Semana1/Sem1_textoBase_ex7_5_p179.py): programa que leia o arquivo CSV criado anteriormente, calculando o valor total em mercadorias e o respectivo crédito de ICMS.
  19. [Testar problemas de encoding](Semana1/Sem1_textoBase_ex7_6_p181.py): algoritmo para leitura e para gravação de arquivos textos usando codificação de caracteres conflitantes, mais detalhes na [W3C](https://www.w3.org/International/questions/qa-what-is-encoding).
  20. [Obter números primos](Semana1/Sem1_textoBase_ep7_1_p182.py): programa que leia um número inteiro N e grave em um arquivo em disco todos os números primos existentes no intervalo fechado [2, N], um número em cada linha.
  21. [Criar arquivo no N números aleatórios](Semana1/Sem1_textoBase_ep7_2_p182.py): gere o arquivo NUMEROS.TXT com 2000 números, um em cada linha, gerados com a função randint no intervalo fechado [1, 100.000].
  22. [Ordenar números aleatórios](Semana1/Sem1_textoBase_ep7_3_p183.py): programa que leia o arquivo NUMEROS.TXT gerado no exercício anterior, colocando-os em uma lista. Ordene a lista utilizando o método Bubble Sort e grave os números ordenados no arquivo “ORDENADOS.TXT”.
  23. [Correção de BUGs](Semana1/ProblemaPratico_4_10.py): explicação do que causa o erro de sintaxe em cada instrução listada.
>  Programação orientada a objetos, prezando pela modularização e reutilização de código
  24. [Classes Point e Vector](Semana2/Sem2_videoaula_POO1.py): conceitos de Orientação a Objeto. Criação das classes _Point_ e _Vector_ com métodos up(), down(), left(), right(), distancia(), subscrição dos métodos para a A classe _Vector_ para aceitar a adição de vetor e operações de produto, além de representação de string canônica. (exercícios 8.12, 8.14 e problema prático 8.8)
  25. [Classes Funcionario e Gerente](Semana2/Sem2_videoaula_POO2-Exercicio.py): trabalhando com herança.
>  Funções recursivas que auxiliam na proposta de soluções para problemas complexos
  26. [Calclular sequência de Fibonacci e Fatorial](Semana3/Sem3_Recursao.py): conceitos de recursão para reselver Fatorial e Fibonacci.
  27. [Comparar tempo entre recursão e iteração](Semana3/Sem3_Recursao_Iteracao.py): comparando os tempos entre iteração e recursão. Conceitos de Memoização para otimizar função recursiva.
  28. [Estudo do capítulo 10 - Recursão](Semana3/Sem3-txtBase.py): analisador de vírus num sistema de arquivos; busca binária em lista (dividir para conquistar); análise experimental de tempo de execução; retornando um dicionário para representar a tabela de frequência de uma lista.
  29. [Estudo da Seção 5.4 - Recursividade](Semana3/Sem3-txtBase2.py): funções variadas: verifica se número é primo; intersecção de duas listas; soma dos elementos de uma lista; busca binária em lista ordenada; verifica se número é par ou ímpar; retorna lista de N números primos; checa divisibilidade entre dois números; conversor de base decimal para binária; cálculo de dígito verificador; valida valor de entrada num intervalo definido; conversor de base decimal para diversas bases - até base 36; inverter sequência de caracteres; verifica palíndromo.
> Estruturas de dados utilizadas para representação, manipulação e armazenamento de dados? **pilhas, filas e árvores**
