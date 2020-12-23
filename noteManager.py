#Classe de gerenciamento de notas
import copy

class NoteManager:
    #Construtor
    def __init__(self):
        self.__notes = []#Lista de tuplas onde o primeiro elemento é a chave(tipo de nota) e o segundo a quantidade

        #Inicialização de todas notas do real aceitas
        self.__notes.append(['2', 0])
        self.__notes.append(['5', 0])
        self.__notes.append(['10', 0]) 
        self.__notes.append(['20', 0])
        self.__notes.append(['50', 0])
        self.__notes.append(['100', 0])
        self.__notes.append(['200', 0])

    #Função de abastecimento
    def fill(self, notes): #Recebe uma lista de tuplas
        tempNotes = copy.deepcopy(self.__notes)
        #Para cada chave/tipo de nota recebida procura a equivalente na lista de notas permitidas/registradas
        #e faz os respectivos abastecimentos
        for i in range(len(notes)):
            hasFind = False
            for k in range(len(tempNotes)):
                if(notes[i][0] == tempNotes[k][0]):
                    tempNotes[k][1] += notes[i][1]   
                    hasFind = True
            if hasFind == False:
                raise ValueError('Chave desconhecida: {}, abastecimento não registrado'.format(notes[i]))
        
        self.__notes = tempNotes

    #Função que tenta realizar um saque
    def tryWithDrawal(self, valor):
        pass

    #Função que realiza o saque e retorna a as notas a serem fornecidas
    def __withDrawal(self):
        pass

    #Função que imprime o atual quantidade de notas
    def show(self):
        print('\n\nNotas disponiveis: ')
        for note in self.__notes:
            print('Notas de {}: {}'.format(note[0], note[1]))