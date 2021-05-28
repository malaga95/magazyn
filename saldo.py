from os import write
import sys
import commands
konto = commands.Account()
konto.add_to_file(sys.argv[1], sys.argv[2])