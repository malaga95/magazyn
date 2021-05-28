#python sprzedaz.py <plik><str identyfikator produktu> <int cena> <int liczba sprzedanych>

                #self.sprzedaz.append(line)
                #print(self.sprzedaz)
import sys
import commands
#from .commands import Sprzedaz
sell = commands.Sprzedaz()
value = (int(sys.argv[3]) * int(sys.argv[4]))
comment = f'Sell of product : {sys.argv2}'
commands.Account.add_to_file(value,comment)
