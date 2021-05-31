#python zakup.py <plik> <str identyfikator produktu> <int cena> <int liczba zakupionych>
import sys
from command.commands import Zakup
buy = Zakup()

if buy.check_balance():
    buy.add_line()