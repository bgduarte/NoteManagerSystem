# NoteManagerSystem
Sistema de gerenciamento de notas para monitorar e controlar a entrada e saída de notas de um caixa eletrônico hipotético.

## Pré-requisitos
Para utilizar é necessario a instalação de [Python](https://www.python.org/)

## Sobre
O sistema consiste em uma classe com um único atributo e quatro funções distintas:
### Atributos
 ### Notas
    __notes
Consiste em uma lista privada de duplas onde o primeiro elemento é o valor de uma nota aceita e o segundo a quantidade atual de notas no caixa.

### Funções
#### Construtor 
```
def __init__(self)
``` 
Não leva nenhum argumento.
- Abastecimento -> fill() : Recebe uma lista de duplas como argumento ondeprimeiro elemento da dupla é o valor de uma nota aceita e o segundo a quantidade atual de notas no caixa.