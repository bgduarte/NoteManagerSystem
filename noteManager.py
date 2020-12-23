#Classe de gerenciamento de notas

def NoteManager():
    #Construtor
    def __init__(self):
        self.__notes = []#Lista de tuplas onde o primeiro elemento é a chave(tipo de nota) e o segundo a quantidade

        #Inicialização de todas notas do real aceitas
        self.__notes.append('2', 0)
        self.__notes.append('5', 0)
        self.__notes.append('10', 0) 
        self.__notes.append('20', 0)
        self.__notes.append('50', 0)
        self.__notes.append('100', 0)
        self.__notes.append('200', 0)

    #Função de abastecimento
    def fill(self, notes): #Recebe uma lista de tuplas

        #Para cada chave/tipo de nota recebida procura a equivalente na lista de notas permitidas/registradas
        #e faz os respectivos abastecimentos
        for i in range(len(notes)):
            for k in range(len(self.__notes)):
                if(notes[i][0] == self.__notes[k][0]):
                    self.__notes[k][1] += notes[i][1]



    #Função que tenta realizar um saque
    def tryWithDrawal(self, valor):
        pass

    #Função que realiza o saque e retorna a as notas a serem fornecidas
    def __withDrawal(self):
        pass

    #Função que imprime o atual quantidade de notas
    def print(self):
