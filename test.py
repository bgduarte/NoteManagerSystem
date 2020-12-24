#Arquivo de testes
from noteManager import NoteManager 
manager = NoteManager()

def printNotesList(notes):
    for note in notes:
        print('Notas de {}: {}'.format(note[0], note[1]))

#TESTES

#Testes de abastecimento
print('\n\nTeste de abastecimento com chave incorreto: ')
notas = [[20, 2],[30, 40], [50, 30]]
try:
    manager.fill(notas)
except Exception as inst:
    print(inst)

print('\n\nTeste de abastecimento: ')
notas = [[20, 2],[50, 5], [100, 3]]
manager.fill(notas)
printNotesList(manager.getNotes())
