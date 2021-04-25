import sys
print(sys.argv)
defined_commands = ('saldo')
command = sys.argv[1:][0]
#value_input = sys.argv[1:][1]

if command == 'saldo':
    print("dziala")


elif command == 'sprzedaz': 
        print("nie dziala")


elif command == 'zakup':
        print("dziala zakup")
elif command == 'konto':
        print("dziala konto")
elif command == 'magazyn':
        print("magazyn dziala")
elif command == 'przeglad':
        print("dziala przeglad")
else: 
    print("niepopoprawna komenda")
'''
lista = sys.argv 
print(lista[1:]
    if lista[2] == "saldo":
    print("dziala")
  '''
