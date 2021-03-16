import sys

from core import write_log, read_log, read_log_all, get_help

command = sys.argv
try:
    if len(command) <= 1:
        read_log_all()
    elif command[1] == 'w':
        write_log(command[2])
    elif command[1] == 'help':
        get_help()
    elif len(command) == 2:
        read_log(command[1])
    elif len(command) == 3:
        read_log(command[1], command[2])
except:
    print('\nОшибка ввода, для помощи введите "help"')
