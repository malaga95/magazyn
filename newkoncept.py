
#New conception of task from segment 5. Depending on inputs from user
#Willing to do whole task with list's had a problem that program didnt save the input.
#lists for inputs
sale_list = []
buy_list = []
account_operations = []
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
            if command == 'saldo':
                value = input ('Podaj wartosc operacji')
                value = int(value)
                commentary = input("Dodaj komentarz do transakcji na koncie")
                account_operations_total.append(f'saldo {value},{commentary}')
                print(account_operations_total)
                #Standard operation for sell and buy, making list with values got from user.
           
            elif command == 'sprzedaz':
                ProductID = input('Podaj kod produktu :')
                product_price = input('Podaj cene produktu :')
                product_price = int(product_price)
                sale_count = input('podaj ilosc produktow :')
                sale_count = int(sale_count)

                sale_list = [ProductID, product_price, sale_count]
                sale_list_total += sale_list
                if ProductID in storage:
                    storage[ProductID] -= sale_count
                    account_operations_total.append(f'Sprzedaz {product_price*sale_count}, {ProductID}')
                else:
                    print('brak produktu w bazie')
            elif command == 'zakup':
                '''
                                            zakup: program pobiera trzy linie: identyfikator produktu (str), cena jednostkowa (int) i liczba sztuk (int). 
                                            Program odejmuje z salda cenę jednostkową pomnożoną przez liczbę sztuk. 
                                            Jeśli saldo po zmianie jest ujemne, cena jest ujemna bądź liczba sztuk jest mniejsza od zero program zwraca błąd. 
                                            Program podnosi stan magazynowy zakupionego towaru'''
                buy_id = input('Podaj kod produktu :')
                buy_price = input('Podaj cene produktu :')
                buy_price = int(buy_price)
                buy_count = input('podaj ilosc produktow :')
                buy_count = int(buy_count)

                
                if buy_id in storage:
                    storage[buy_id] += buy_count
                    account_operations_total.append(f'Zakup {buy_price*buy_count}, {buy_id}')
                else:
                    storage[buy_id] = buy_count
                #buy_list = [ProductID, buy_price, buy_count]
                #buy_list_total =+ buy_list
                print(storage)
              
            elif command == 'end':

                print('Lista operacji przeprowadzonych na koncie : \n', account_operations_total)
                print('Lista sprzedaży : \n', sale_list)
                print('Lista zakupow :\n', buy_list)

    else :
        print("podano niepoprawna komende")
        break
