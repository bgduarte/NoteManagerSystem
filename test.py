#Base para os de testes
from noteManager import NoteManager 
manager = NoteManager()

def printNotesList(notes):
    if(len(notes) == 0):
        print('Não há notas')
    else:
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
notas = [[20, 3],[50, 5], [100, 3]]
manager.fill(notas)
printNotesList(manager.getNotes())

#Testes de saque
print('\nTeste saque de 40 reais: ')
printNotesList(manager.withDrawal(40))
print('Estado da maquina depois da operação: ')
printNotesList(manager.getNotes())


print('\nTeste saque de 70 reais: ')
printNotesList(manager.withDrawal(70))
print('Estado da maquina depois da operação: ')
printNotesList(manager.getNotes())

print('\nTeste saque de 70 reais sem notas suficientes: ')
printNotesList(manager.withDrawal(70))
print('Estado da maquina depois da operação: ')
printNotesList(manager.getNotes())

print('\nTeste de saque com um valor muito alto(800): ')
printNotesList(manager.withDrawal(800))
print('Estado da maquina depois da operação: ')
printNotesList(manager.getNotes())