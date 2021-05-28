#python zakup.py <plik> <str identyfikator produktu> <int cena> <int liczba zakupionych>
import sys
import commands
buy = commands.Zakup()
if buy.check_balance():
    buy.add_line()