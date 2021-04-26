import sys
command = sys.argv[1:][0]
#value_input = sys.argv[1:][1]
#setting allowed commands on input
allowed_commands = ('saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad')
if command in allowed_commands:
    print(sys.argv[1])  
    #Instruction for command saldo
    if sys.argv[1] == ('saldo'):
        sys.argv[2] = int(sys.argv[2])
        #setting new names for input's
        value = sys.argv[2]
        commentary = sys.argv[3]
        #Safetycheckprint
        #print(value, commentary)
        
        #Instruction for command sprzedaz
    elif sys.argv[1] == ('sprzedaz'):    
            
            sys.argv[3] = int(sys.argv[3])
            sys.argv[4] = int(sys.argv[4])
        #Instruction for command zakup
    elif sys.argv[1] == ('zakup'):
            sys.argv[3] = int(sys.argv[3])
            sys.argv[4] = int(sys.argv[4])
    else:
        print("Nie rozpoznano komendy")








'''
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
''''''
lista = sys.argv 
print(lista[1:]
    if lista[2] == "saldo":
    print("dziala")
  '''
