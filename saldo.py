from os import write
class Account():
    def __init__(self):
        self.account = []
        self.add_line()
    def add_line(self):
        value = sys.argv[2]
        comment = sys.argv[3]
        self.account.append(value)
        self.account.append(comment)
    def open_file(self):
        with open('konto.txt', 'a') as file:
            file.write(str(sys.argv[2]) + ',' + str(sys.argv[3]) + '\n')
import sys
#sys.argv[1]
#sys.argv[2]
#sys.argv[3]
#print(sys.argv[2])
#with open ('konto.txt', 'r') as file:
#    for line in file.readlines():
#        print(line)
#with open ('konto.txt', 'w') as file:
#    for line in file.readlines():
#        file.write(sys.argv[2] + sys.argv[3] + '\n')       
konto = Account()
print(konto.account)
konto.open_file()