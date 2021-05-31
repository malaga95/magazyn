#python sprzedaz.py <plik><str identyfikator produktu> <int cena> <int liczba sprzedanych>

                #self.sprzedaz.append(line)
                #print(self.sprzedaz)
import sys
from command.commands import Account,Sprzedaz
#from .commands import Sprzedaz
sell = Sprzedaz()
acc = Account()
value = (int(sys.argv[3]) * int(sys.argv[4]))
comment = sys.argv[2]
print(value,comment)
acc.add_to_file(value,comment)
