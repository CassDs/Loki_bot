from iqoptionapi.stable_api import IQ_Option
from config import controle, matrix
import logging 
from windows import home, login, modo, perfil, painel
from windows import banner2
import os
import time
import sys

ContConct = 0
user = ''
password = ''
os.system('cls')
concx = False

matrix()
home()
login()
while(concx == False):
    banner2()
    t = controle(user,password)
    user, password = t
    logging.disable(level=(logging.DEBUG))
    IQ = IQ_Option(user,password)
    IQ.connect()
    if IQ.check_connect() == False:
        banner2()
        for i in range(42):
            time.sleep(0.1)
            sys.stdout.write("\rConectando: %d%%" % i)
            while (i > 101):
                os.system('cls')
        sys.stdout.flush()
        print('\nErro ao se conectar...')
        ContConct +=1
        time.sleep(2)
        if (ContConct == 4):
            banner2()
            print('Verfique sua conexão com a internet ou seu e-mail/senha...')
            print('Por questões de segurança o sistema será encerrado!')
            time.sleep(7)
            banner2()
            print('Sistema encerrado!!!')
            time.sleep(2)
            exit()

    else:
        banner2()
        for i in range(101):
            time.sleep(0.1)
            sys.stdout.write("\rConectando: %d%%" % i)
            while (i > 101):
                os.system('cls')
        sys.stdout.flush()
        banner2()
        print('Você esta conectado no servidor da IQ Option!')
        time.sleep(4)
        t = True
        break
modo(IQ)
painel(IQ)


