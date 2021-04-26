import sys
command = sys.argv[1:][0]
#value_input = sys.argv[1:][1]
#setting allowed commands on input
allowed_commands = ('saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad', 'end')
while True:

        if command in allowed_commands:
                
                #Instruction for command saldo
                if sys.argv[1] == ('saldo'):
                        sys.argv[2] = int(sys.argv[2])
                        #setting new names for input's
                        value = sys.argv[2]
                        commentary = sys.argv[3]
                        saldo = {}

                        #Safetycheckprint
                        #print(value, commentary)
                        
                        #Instruction for command sprzedaz
                elif sys.argv[1] == ('sprzedaz'):    
                        #converting variables to proper type.
                        sys.argv[3] = int(sys.argv[3])
                        sys.argv[4] = int(sys.argv[4])
                        #Adding names of values
                        ProductID = sys.argv[2]
                        product_price = sys.argv[3]
                        sale_count = sys.argv[4]
                        sale = {}

                        #Instruction for command zakup
                elif sys.argv[1] == ('zakup'):
                        #converting variables to proper type.
                        sys.argv[3] = int(sys.argv[3])
                        sys.argv[4] = int(sys.argv[4])
                        #Adding names of values
                        ProductID = sys.argv[2]
                        product_price = sys.argv[3]
                        buy_count = sys.argv[4]
                        buy = {}
        elif command == 'end':
                break
        else:
                continue
        
        
'''else: 
print("podano niepoprawna komende")
continue'''







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
