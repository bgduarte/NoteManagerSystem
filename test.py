#Arquivo de testes
from noteManager import NoteManager 
noteM = NoteManager()

#TESTES

#Testes de abastecimento
print('\n\nTeste de abastecimento com chave incorreto: ')
notas = [['20', 2],['fe', 40], ['50', 30]]
try:
    noteM.fill(notas)
except Exception as inst:
    print(inst)


notas = [['20', 2],['50', 40], ['100', 30]]
try:
    noteM.fill(notas)
except Exception as inst:
    print(inst)



noteM.show()