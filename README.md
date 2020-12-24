# NoteManagerSystem
Sistema de gerenciamento de notas para monitorar e controlar a entrada e saída de notas de um caixa eletrônico hipotético.

## Pré-requisitos
Para utilizar é necessario a instalação de [Python](https://www.python.org/)

## Sobre
O sistema consiste em uma classe com um único atributo e quatro funções distintas:
### Atributos
 #### Notas
    __notes
Consiste em uma lista privada de duplas onde o primeiro elemento é o valor de uma nota aceita e o segundo a quantidade atual de notas no caixa.

### Funções
#### Construtor 
```
def __init__(self):
``` 
Não leva nenhum argumento.

#### Abastecimento 
    def fill(self, notes): 
Recebe uma lista de duplas de inteiros como argumento, onde primeiro elemento da dupla é o valor/tipo de nota e o segundo a quantidade de notas desse tipo. Após isso percorre a lista de notas fazendo os devidos abastecimentos.  Caso não haja correspondencia nas notas passadas como argumento, a função gera uma excessão do tipo _ValueError_ e cancela a operação. Não possui nenhum retorno.

#### Saque
    def withDrawal(self, value):
Recebe um valor como argumento e retorna uma lista com as notas necessárias para fazer o saque além de subtrai-las da lista de notas atual. Caso não seja possivél realizar o saque retorna uma lista vazia.

#### Get Notas
    def getNotes(self):
Não possui argumento e retorna uma cópia da lista atual de notas.

## Como utilitar
Para utilizar o sistema instancie a classe _noteManager_ no arquivo _noteManager.py_ e chame as funções de abastecimento e saque conforme a documentação acima. Há também um arquivo _test.py_ que possui alguns testes exemplo. Basta executa-lo para verificar algumas das funcionalidades da classe

## Autor:
Bernardo Gomes Duarte