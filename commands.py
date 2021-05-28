import sys
class Account:
    def __init__(self):
        self.account = []
    #    self.add_line()
    #def add_line(self):
    #    value = sys.argv[1]
    #    comment = sys.argv[2]
    #    self.account.append(value)
    #    self.account.append(comment)
    def add_to_file(self, value, comment):
        with open('konto.txt', 'a') as file:
            file.write(str(value) + ',' + str(comment) + '\n')



class Sprzedaz:
    def __init__(self):
        self.sprzedaz = []
        self.add_line()
        #id = self.product_id
        #price = self.product_price
        #count = self.product_count
    
    def add_line(self, id, price, count):
        self.id = sys.argv[2]
        self.price = sys.argv[3]
        self.count = sys.argv[4]
        with open (str(sys.argv[1]), 'r') as file:
            for line in file.readlines():
                print(line)
        with open (str(sys.argv[1]), 'a') as file:
            file.write(self.id + ',' + self.price + ',' + self.count + '\n')
    def check_storage():
        pass
    def remove_from_storage():
        pass

class Zakup:
    balance = 0
    def __init__(self):
        self.id = sys.argv[2]
        self.price = sys.argv[3]
        self.count = sys.argv[4]
        #self.check_balance()
        #id = self.product_id
        #price = self.product_price
        #count = self.product_count
    
    def add_line(self):
        if self.id != 'buy_list.txt':
            print('Wybrano złą nazwe pliku, aby przeprowadzic zakup uzyj pliku buy_list.txt')
        with open (str(sys.argv[1]), 'r') as file:
            for line in file.readlines()[1:]:
                print(line)
        with open (str(sys.argv[1]), 'a') as file:
            file.write(self.id + ',' + self.price + ',' + self.count + '\n')
                #self.sprzedaz.append(line)
                #print(self.sprzedaz)
    
    def check_storage():
        pass
    
    def check_balance(self):
        check = Balance()
        total_price = int(self.price) * int(self.count)
        if total_price > check.check_balance():
            print('nie posiadasz wystarczajaco srodkow na koncie aby dokonac zakupu')
            return False
        else:
            with open ('konto.txt', 'a') as file:
                file.write(str((total_price) * -1) + ',' + 'Buy of product' + str(self.id) + '\n')
                return True

    #def check_balance(self):
    #    val = int(self.price) * int(self.count)
    #    with open ('konto.txt', 'r') as file:
    #            check = Balance()
    #            check.get_balance(self.balance)
    #            if val > self.balance:
    #                print('nie posiadasz wystarczajacych srodkow na zakup produktu')
    #            else:
    #                set_amount = self.balance - val
    #                with open ('konto.txt', 'a') as file:
    #                    file.write({{-val} + ',' + 'Zakup' + {self.id}})

class Storage:
    def __init__(self):
        with open ('storage.txt', 'r') as file:
            for line in file.readlines():
                id = line.split(',')[0]
                count = line.split(',')[1]
                print(id,count)
                if sys.argv[2:] == 'id':
                    print(count)

        


class Balance:
    balance = 0
    def get_balance(self):
        with open ('konto.txt', 'r') as file:
            for line in file.readlines():
                val = line.split(',')[0]
                comment = line.split(',')[1]
                self.balance += int(val)
    def check_balance(self):
        self.get_balance()
        return self.balance


class Overview:
    def __init__(self):
        print("Lista zakupów :")
        with open ('buy_list.txt', 'r') as file:
            for line in file.readlines():
                print(line)
        print('Lista sprzedazy :')
        with open ('sale_list.txt', 'r') as file:
            for line in file.readlines():
                print(line)
        print('Przeglad operacji na koncie :')
        with open ('konto.txt', 'r') as file:
            for line in file.readlines():
                print(line)
        print('Stan magazynu :')
        with open ('storage.txt', 'r') as file:
            for line in file.readlines():
                print(line)