#Classe de gerenciamento de notas
import copy
import math

class NoteManager:
    #Construtor
    def __init__(self):
        self.__notes = []#Lista de duplas onde o primeiro elemento é a chave(valor da nota) e o segundo a quantidade

        #Inicialização de todas notas do real aceitas. Também define a ordem na qual as notas são retiradas
        self.__notes.append([100, 0])
        self.__notes.append([50, 0]) 
        self.__notes.append([20, 0])
        self.__notes.append([10, 0])

    #Função de abastecimento
    def fill(self, notes): #Recebe uma lista de duplas
        tempNotes = copy.deepcopy(self.__notes)
        
        #Para cada chave/tipo de nota recebida procura a equivalente na lista de notas permitidas/registradas
        #e faz os respectivos abastecimentos
        for i in range(len(notes)):
            hasFind = False #Variavel que controla se se todas as notas na lista tem uma correspondente
            for k in range(len(tempNotes)):
                if(notes[i][0] == tempNotes[k][0]):
                    tempNotes[k][1] += notes[i][1]   
                    hasFind = True
            if hasFind == False:
                raise ValueError('Nota desconhecida: {}, abastecimento não registrado'.format(notes[i][0]))
        
        self.__notes = tempNotes

    #Função que de saque
    def withDrawal(self, value):
        withDrawalNotes = []
        tempNotes = copy.deepcopy(self.__notes)

        for note in tempNotes:
            noteAmount = math.floor(value/note[0]) # Função floor simula divisão propia de inteiros
            if(noteAmount != 0):
                if(noteAmount > note[1]):#Se a quantidade sugerida daquelas notas for maior que as notas disponiveis
                    noteAmount = note[1]
                withDrawalNotes.append([note[0], noteAmount])
                value -= note[0] * noteAmount
                note[1] -= noteAmount
        
        if(value != 0):#Se o valor do saque não foi satisfeito cancela a operaçao e retorna um lista sem notas
            withDrawalNotes = []
        else:
            self.__notes = tempNotes
        
        return withDrawalNotes

    #Função que retorna a quantidade de notas atual
    def getNotes(self):
        return copy.deepcopy(self.__notes)