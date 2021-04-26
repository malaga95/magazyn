
#New conception of task from segment 5. Depending on inputs from user
#Willing to do whole task with list's had a problem that program didnt save the input.
#lists for inputs
sale_list = []
buy_list = []
account_operations = []
#lists for storage
sale_list_total = []
buy_list_total = []
account_operations_total = []
while True:
    command = input('Co chcesz wprowadzic ?')
    #Commands that are allowing program to work
    allowed_commands = ('saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad', 'end')
    for command in allowed_commands:
            if command == 'saldo':
                value = input ('Podaj wartosc operacji')
                value = int(value)
                commentary = input("Dodaj komentarz do transakcji na koncie")
                account_operations = [value, commentary]
                account_operations_total += account_operations
                print(account_operations_total)
                break
                #Standard operation for sell and buy, making list with values got from user.
            if command == 'sprzedaz':
                ProductID = input('Podaj kod produktu :')
                product_price = input('Podaj cene produktu :')
                product_price = int(product_price)
                sale_count = input('podaj ilosc produktow :')
                sale_count = int(sale_count)
                sale_list = [ProductID, product_price, sale_count]
                sale_list_total += sale_list
                break
            if command == 'zakup':
                ProductID = input('Podaj kod produktu :')
                buy_price = input('Podaj cene produktu :')
                buy_price = int(buy_price)
                buy_count = input('podaj ilosc produktow :')
                buy_count = int(buy_count)
                buy_list = [ProductID, buy_price, buy_count]
                buy_list_total =+ buy_list
                break
            if command == 'end':

                print('Lista operacji przeprowadzonych na koncie : \n', account_operations_total)
                print('Lista sprzedaży : \n', sale_list)
                print('Lista zakupow :\n', buy_list)

    else :
        print("podano niepoprawna komende")
