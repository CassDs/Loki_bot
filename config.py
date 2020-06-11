def carregamento():
    def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r\033[32m%s |%s %s%% %s\033[m' % (prefix, bar, percent, suffix), end = '\r')
        # Print New Line on Complete
        if iteration == total: 
            print()


    from time import sleep
    import os
    import time
    # A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Conectando:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Carregando:', suffix = 'Complete', length = 50)

def controle(x,y):
    import getpass
    print('#Por questões de privacidade sua senha não será visível na tela#')
    print()
    x = input('Digite seu e-mail:')
    y = getpass.getpass('Digite sua senha:')
    z = x
    w = y
    return z,w   

import time
from datetime import datetime, timedelta
from dateutil import tz


def timestamp_converter(x,b):
    hora = datetime.strptime(datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    if(b == 'digital-option'):
        hora = hora.replace(tzinfo=tz.gettz('GMT-3'))
    else:
        hora = hora.replace(tzinfo=tz.gettz('GMT-3'))
        
    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6] #Conversor de horas

def get_time_now(API, format='%d/%m/%Y'):
    timestamp = API.get_server_timestamp()
    return datetime.fromtimestamp(timestamp)

def resultados_trader(result):
    arq = open('Resultados_Trade.txt', 'r')
    dados = arq.readlines()
    dados.append(result)
    dados.append('\n')
    arquivo = open('Resultados_Trade.txt', 'w')
    arquivo.writelines(dados)
    arquivo.close()       

def get_time_now(API, format='%d/%m/%Y'):
    timestamp = API.get_server_timestamp()
    return datetime.fromtimestamp(timestamp)

def matrix():
    import random as r
    import time, os

    symbols = ['0','1',' ',' ']
    line = []
    counter = 0
    os.system('color A')
    print('O programa está iniciando...')
    time.sleep(3)
    os.system('cls')
    for i in range(118):
        x = r.randint(0,3)
        line.append(symbols[x])

        counter += 1

    for i in range(500):
        if counter % 5 == 0:
            r_symbols = [r.randint(0,117) for x in range(10)]
            for i in r_symbols:
                line[i] = symbols[r.randint(0,3)]
        print(*line)
        counter+=1
        time.sleep(0.01)
    os.system('cls')    
        

