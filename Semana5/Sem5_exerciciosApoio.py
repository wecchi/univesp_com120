"""
    Fazer os exercícios 2, 3, 7, 8, 13 e 20 (p. 158)
    Ziviani, N. Projeto de Algoritmos: com Implementações em Pascal e C – 3ª edição revista e ampliada.
    São Paulo: Cengage Learning Brasil, 2018. 9788522126590.
    Disponível em: https://integrada.minhabiblioteca.com.br/#/books/9788522126590/. Acesso em: 08 Nov 2020
"""
## 2. Invente um vetor-exemplo de entrada para demonstrar que ordenação por Seleção é um método instável.
# Mostre os passos da execução do algoritmo até que a estabilidade seja violada. Note que quanto menor for o vetor
# que você inventar, mais rápido você vai resolver a questão

## 3. Modifique o algoritmo de ordenação por inserção do Programa 4.4 de forma que ele utilize a busca binária para
# encontrar a posição de inserção de um ele-mento no vetor destino. Considerando o número C(n) de comparações efetuadas,
# determine a complexidade do algoritmo obtido (Patrocínio Júnior, 2003).
# procedure Insercao (var A: TipoVetor ; n: TipoIndice ) ;
# var i , j : TipoIndice ;
# x : TipoItem;
# begin
# for i := 2 to n do
#   begin
#   x := A[ i ] ;
#   j := i − 1;
#   A[0] := x ; { sentinela }
#   while x.Chave < A[ j ] .Chave do
#       begin
#       A[ j + 1] := A[ j ] ;
#       j := j − 1;
#       end;
#   A[ j + 1] := x;
#   end;
#end;


## 7. Reorganize os elementos de um vetor contendo números inteiros de forma que todos os números negativos precedam os
# não-negativos (Guedes Neto, 2003). Indique como um dos métodos de ordenação apresentados na Seção 4.1 pode ser
# alterado para conseguir tal organização em tempo proporcional ao número de elementos do vetor. Estenda sua solução
# para garantir que haja zeros entre os números positivos e os números negativos

## 8. Quicksort não é um algoritmo estável (Guedes Neto, 2003). Que tipo de transformação você poderia fazer nas chaves
# para que ele se torne um algoritmo estável? Discuta se a transformação proposta é independente da natureza da chave.

## 13. Quicksort
# a) Mostre como o vetor A B A B A B A é particionado quando se escolhe o elemento do meio, A[(esq + dir) div 2],
# como pivô.
# b) Mostre as etapas de funcionamento do Quicksort para ordenar as chaves Q U I C K S O R T.
# Considere que o pivô escolhido é o elemento do meio, A[(esq + dir) div 2].

## 20. Mergesort (Menezes, 2010).
# a) Implemente o procedimento Merge do Programa 2.9.
# procedure Mergesort (var A: array[ 1 . .n] of integer ; i , j : integer) ;
# begin
#   i f i < j then begin
#       m := ( i + j )/2;
#       Mergesort (A, i , m) ;
#       Mergesort (A, m+1, j ) ;
#       Merge (A, i , m, j ) ; { Intercala A[i . .m] e A[m+1.. j ] em A[i . . j ] }
#       end;
# end;
# b) Compare o desempenho do procedimento Mergesort implementado no item anterior com o procedimento Quicksort do
# Programa 4.7.
# procedure QuickSort (var A: TipoVetor ; n: TipoIndice ) ;
# {−− Entra aqui o procedimento Particao do Programa 4.6} −−}
#   procedure Ordena (Esq, Dir : TipoIndice ) ;
#   var i , j : TipoIndice ;
#   begin
#       particao (Esq, Dir , i , j ) ;
#       if Esq < j then Ordena (Esq, j ) ;
#       if i < Dir then Ordena ( i , Dir ) ;
#   end;
# begin
#   Ordena (1 , n) ;
# end;