from os import write
from typing import Text
#New conception of task from segment 5. Depending on inputs from user
#Willing to do whole task with list's had a problem that program didnt save the input.
#lists for inputs
sale_list = []
buy_list = []
account_operations = []
balance = 0
#lists for storage
sale_list_total = []
buy_list_total = []
storage = {}
account_operations_total = []

allowed_commands = ('saldo', 'sprzedaz', 'zakup', 'end')
while True:
    command = input('Co chcesz wprowadzic ?')
    #Commands that are allowing program to work
    
    if command in allowed_commands:
            #with open ("sale_list.txt", "r") as file:
                #for line in file.readlines():
                #    file.write(str(product_id) + ',' + (product_price) + ',' + (sale_count))
 
            if command == 'saldo':
                from .saldo import Account

           
            #    value = input ('Podaj wartosc operacji')
            #    value = int(value)
            #    commentary = input("Dodaj komentarz do transakcji na koncie")
            #    balance += value
            #    account_operations_total.append(f'saldo {value},{commentary}')
            #    print(account_operations_total)
            #    print(balance)
            #Standard operation for sell and buy, making list with values got from user.
            
            elif command == 'sprzedaz':
                product_id = input('Podaj kod produktu :')
                product_price = input('Podaj cene produktu :')
                product_price = int(product_price)
                
                if product_price < 0:
                    print("Podano ujemna cene sprzedazy, aby kupic uzyj komendzy zakup !")
                    break
                
                sale_count = input('podaj ilosc produktow :')
                sale_count = int(sale_count)
                
                if sale_count < 0:
                        print("wprowadzono niepoprawna wartość")
                        break
                
                if sale_count in storage < 0:
                        print("Chcesz sprzedac za duza ilosc produktow")
                        break
                with open ("sale_list.txt", "w") as file:
                    for product in sale_list_total:
                        file.write(str(product_id) + ',' + (product_price) + ',' + (sale_count))

                sale_list =  [product_id, product_price, sale_count]
                sale_list_total += sale_list
                
                if product_id in storage:
                    
                    storage [product_id] -= sale_count
                    account_operations_total.append(f'Sprzedaz {product_price*sale_count},  {product_id}')
                    balance += (product_price*sale_count)
                    print(balance)

                else:
                    print('brak produktu w bazie')
            elif command == 'zakup':
                buy_id = input('Podaj kod produktu :')
                buy_price = input('Podaj cene produktu :')
                buy_price = int(buy_price)

                if buy_price < 0:
                    print("Podano ujemna cene zakupu, aby sprzedac uzyj komendzy sprzedaz !")
                    break

                buy_count = input('podaj ilosc produktow :')
                buy_count = int(buy_count)
                short = (balance - buy_count*buy_price) * -1

                if balance < (buy_count*buy_price):
                    print(f'Brakuje Ci {short} pieniedzy aby zakupic porzadana ilosc produktu')
                    break

                if buy_count <= 0:
                    print("wprowadzono niepoprawna wartosc")
                    break             
                buy_list =  [buy_id, buy_price, buy_count]
                buy_list_total += buy_list

                if buy_id in storage:
                    storage[buy_id] += buy_count
                    account_operations_total.append(f'Zakup {buy_price*buy_count}, {buy_id}')
                    balance -= (buy_price*buy_count)

                else:
                    storage[buy_id] = buy_count
                    account_operations_total.append(f'Zakup {buy_price*buy_count}, {buy_id}')
                    balance -= (buy_price*buy_count)

                #buy_list =  product_id, buy_price, buy_count]
                #buy_list_total =+ buy_list
                print(storage)
                print(balance)            

            elif command == 'end':

                print('Lista operacji przeprowadzonych na koncie : \n', account_operations_total)
                print('Lista sprzedaży : \n', sale_list_total)
                print('Lista zakupow :\n', buy_list_total)
                print(balance)

    else :
        print(f"podano niepoprawna komende, dozwolone komendy to {allowed_commands}")
        break
with open ("sale_list.txt" "w") as file:
    for product in sale_list_total:
        file.write()
