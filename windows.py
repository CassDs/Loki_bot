Version = '0.1.9'
def banner1():
    import os
    os.system('cls')
    print('\u001b[32;1m$$\       $$$$$$\  $$\   $$\   $$\         $$$$$$$\   $$$$$$\ $$$$$$$$\ ')
    print('\u001b[32;1m$$ |     $$$ __$$\ $$ | $$  |$$$$ |        $$  __$$\ $$$ __$$\\__ $$ __|')
    print('\u001b[32;1m$$ |     $$$$\ $$ |$$ |$$  / \_$$ |        $$ |  $$ |$$$$\ $$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$\$$\$$ |$$$$$  /    $$ |        $$$$$$$\ |$$\$$\$$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$ \$$$$ |$$  $$<     $$ |        $$  __$$\ $$ \$$$$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$ |\$$$ |$$ |\$$\    $$ |        $$ |  $$ |$$ |\$$$ |  $$ |   ')
    print('\u001b[32;1m$$$$$$$$\\$$$$$$   /$$ | \$$\ $$$$$$\       $$$$$$$  |\$$$$$$ /   $$ |   ')
    print('\u001b[32;1m\________|\______/ \__|  \__|\______|      \_______/  \______/   \__|   Version - {}' .format(Version))
    print("____________________________________________________________________________________________________")
    print('Bem vindo a versão teste do L0k1 Bot!\nEste sistema esta na versão {}.' .format(Version))
    print('Ele se conecta com a IQ Option e automatiza sua lista de sinais realizando aberturas de ordens para compra.')
    print('Qualquer prejuizo é de total responsabilidade de seu usuário.')
    print('Aprecie com moderação!!!')
    print()

def banner2():
    import os
    os.system('cls')
    print('\u001b[32;1m$$\       $$$$$$\  $$\   $$\   $$\         $$$$$$$\   $$$$$$\ $$$$$$$$\ ')
    print('\u001b[32;1m$$ |     $$$ __$$\ $$ | $$  |$$$$ |        $$  __$$\ $$$ __$$\\__ $$ __|')
    print('\u001b[32;1m$$ |     $$$$\ $$ |$$ |$$  / \_$$ |        $$ |  $$ |$$$$\ $$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$\$$\$$ |$$$$$  /    $$ |        $$$$$$$\ |$$\$$\$$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$ \$$$$ |$$  $$<     $$ |        $$  __$$\ $$ \$$$$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$ |\$$$ |$$ |\$$\    $$ |        $$ |  $$ |$$ |\$$$ |  $$ |   ')
    print('\u001b[32;1m$$$$$$$$\\$$$$$$   /$$ | \$$\ $$$$$$\       $$$$$$$  |\$$$$$$  /  $$ |   ')
    print('\u001b[32;1m\________|\______/ \__|  \__|\______|      \_______/  \______/   \__|   Version - {}' .format(Version))
    print("____________________________________________________________________________________________________")
    print()

def home():
    from config import carregamento
    import time
    import os
    os.system('cls')

    print('\u001b[32;1m$$\       $$$$$$\  $$\   $$\   $$\         $$$$$$$\   $$$$$$\ $$$$$$$$\ ')
    print('\u001b[32;1m$$ |     $$$ __$$\ $$ | $$  |$$$$ |        $$  __$$\ $$$ __$$\\__ $$ __|')
    print('\u001b[32;1m$$ |     $$$$\ $$ |$$ |$$  / \_$$ |        $$ |  $$ |$$$$\ $$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$\$$\$$ |$$$$$  /    $$ |        $$$$$$$\ |$$\$$\$$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$ \$$$$ |$$  $$<     $$ |        $$  __$$\ $$ \$$$$ |  $$ |   ')
    print('\u001b[32;1m$$ |     $$ |\$$$ |$$ |\$$\    $$ |        $$ |  $$ |$$ |\$$$ |  $$ |   ')
    print('\u001b[32;1m$$$$$$$$\\$$$$$$   /$$ | \$$\ $$$$$$\       $$$$$$$  |\$$$$$$  /  $$ |   ')
    print('\u001b[32;1m\________|\______/ \__|  \__|\______|      \_______/  \______/   \__|   Version - {}' .format(Version))
    print('____________________________________________________________________________________________________')
    print()   
    print('                           _         ______       _            ')    
    print('     /\                   | |       |  ____|     | |           ')   
    print('    /  \   _ __   ___ _ __| |_ ___  | |__   _ __ | |_ ___ _ __ ')   
    print("   / /\ \ | '_ \ / _ \ '__| __/ _ \ |  __| | '_ \| __/ _ \ '__|")   
    print('  / ____ \| |_) |  __/ |  | ||  __/ | |____| | | | ||  __/ |   ')   
    print(' /_/    \_\ .__/ \___|_|   \__\___| |______|_| |_|\__\___|_|   ')   
    print('          | |                                                  ')   
    print('          |_|                                                  ')   



    x = input()
    carregamento()
    time.sleep(2)     

def data():
    from datetime import date
    data_atual = date.today()
    return data_atual

def data_comp(data):

    from datetime import date

    DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    ]


    data = date.today()
    dat = str(data)
    x = dat.split('-')
    x = list(x)
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    data = date(year = year, month = month, day = day)
    indice_da_semana = data.weekday()
    dia_da_semana = DIAS[indice_da_semana]
    dia = str(dia_da_semana)

    return (dia)




def login():
    import time
    import os
    os.system('cls')
    banner1()
    print('')
    op = ''
    print('Deseja realizar o login?[S/N]')
    op = input('=>')
    while((op != 'S') and (op != 's') and (op != 'N') and (op != 'n')):
        banner1()
        print('Caractere inválido!!!')
        print('Deseja realizar o login?[S/N]')
        op = input('=>')
    if ((op == 'S') or (op == 's')):
        banner2()
        print('Carregando informações para efetuar o login...')
        time.sleep(3)
    elif((op == 'N') or (op == 'n')):
        banner2()
        print('Sistema sendo finalizado...')
        time.sleep(3)  
        banner2()
        print('Sistema encerrado!!!')  
        time.sleep(2)  
        exit()    
    
def modo(API):
    import os
    import time
    import sys
    os.system('cls')
    banner2()
    print('Escolha o modo para operações:')
    print('\u001b[32;1mDigite [R] para\033[m \u001b[42mREAL\033[m \u001b[32;1mou [T] para\033[m \u001b[42mTREINAMENTO \033[m')
    op = ''
    op = input('\u001b[32;1m=>')
    while((op != 'R') and (op != 'r') and (op != 'T') and (op != 't')):
        banner2()
        print('Comando inválido!!!')
        print('\u001b[32;1mDigite [R] para\033[m \u001b[42mREAL\033[m \u001b[32;1mou [T] para\033[m \u001b[42mTREINAMENTO \033[m')
        op = input('\u001b[32;1m=>')                                                                    
    if((op == 'T') or (op == 't')):
        MODE = 'PRACTICE'
        API.change_balance(MODE)
        banner2()
        print('Você ativou o modo\033[m \u001b[42mTREINAMENTO\033[m')
        time.sleep(5)
        banner2()
        for i in range(101):
            time.sleep(0.1)
            sys.stdout.write("\rCarregando dados do perfil: %d%%" % i)
            while (i > 101):
                os.system('cls')
        os.system('cls') 
        banner2()          
        print('Dados carregados com sucesso...')    
        time.sleep(3)    
    elif((op == 'R') or (op == 'r')):  
        MODE = 'REAL'
        API.change_balance(MODE)
        banner2()
        print('Você ativou o modo\033[m \u001b[42mREAL\033[m')
        print('')
        print('\u001b[32;1m#Atenção#')
        print('Seja bastante cauteloso, escolha bem seus sinais e mantenha o gerenciamento!')
        time.sleep(5)
        banner2()
        for i in range(101):
            time.sleep(0.1)
            sys.stdout.write("\rCarregando dados do perfil: %d%%" % i)
            while (i > 101):
                os.system('cls')
        os.system('cls') 
        banner2()       
        print('Dados carregados com sucesso...')    
        time.sleep(3)  
def perfil(API): 
    import os
    import time
    os.system('cls')
    x = data()
    banner2()
    perfil = API.get_profile_ansyc()
    print('\u001b[32;1mVoce esta logado como: | \033[m\u001b[34m{}\033[m\u001b[32;1m\033[m\u001b[32;1m | {}' .format(perfil['name'],x))
    print('\u001b[32;1mSaldo:\033[m \u001b[42;1m {} \033[m \u001b[32;1m' .format(API.get_balance()))
    print('-----------------------------------------------------------------------------------------------------')
    print('')
    
def painel(API):
    from config import get_time_now
    import os
    import time
    x = data()
    pares = 'digital-option'
    stopW = 2
    stopL = 4
    galex = 1.5
    x = data_comp(x)
    a = 0
    while(True):
        if((x == 'Sábado') or (x == 'Domingo')):
            os.system('cls')
            perfil(API)
            print('\u001b[32;1mEscolha as opções abaixo digitando os respectivos numeros para a sua escolha:')
            print('\n[1] - {Fazer trader}     [2] - {Usar Lista}     [3] - {Configurações}     [4] - {Sair}     ')
            print('=========================================================================================')
            print('                                    MERCADO EM OTC')
            print('                                       PAYOUT M1')
            print('=========================================================================================')
            paridades(API, timeframe=1)
            op = ''
            op = input('Escolha sua opção=>')
        else:
            os.system('cls')
            perfil(API)
            print('\u001b[32;1mEscolha uma das opções abaixo digitando seu respectivos numeros:')
            print('\n[1] - {Fazer trader}     [2] - {Usar Lista}     [3] - {Configurações}     [4] - {Sair}     ')
            print('=========================================================================================')
            print('                                       PAYOUT M1')
            print('=========================================================================================')
            op = ''
            paridades(API, timeframe=1)
            op = input('Escolha sua opção=>')        
        if(op == '1'):
            loop = True
            while(loop):
                a = trader(API,a)
                loop = a
                break
        elif(op == '2'):
            loop = True
            while(loop):
                a = painel_automatizador(API,stopW,stopL,pares,galex,a)
                loop = a
                break
        elif(op == '3'):
            loop = True
            while(loop):
                pares,stopW,stopL,galex,a = config(API,pares,stopW,stopL,galex,a)
                loop = a
                break
        elif(op == '4'):
            banner2()
            print('Sistema sendo finalizado...')
            time.sleep(3)  
            banner2()
            print('Sistema encerrado!!!')  
            time.sleep(2)  
            exit()      
        else:
            print('Opção invalida!!!')    
            time.sleep(3)


def trader(API, loop):
    import os
    import time
    horas = ''
    pares = ''
    ativo = ''
    direcao = ''
    valor = 0
    timeM = 0
    gale = 0
    galex = 0
    cont = 0
    while(cont == 0):
        os.system('cls')
        perfil(API)
        print('#Você esta fazendo o trader por conta própria#')
        print('#É altamente recomendado observar o gráfico junto com o bot#')
        print('')
        ativo,horas,direcao,valor,gale,pares,timeM,galex = dados_compra(ativo,horas,direcao,valor,gale,pares,timeM,galex)
        if pares == 'turbo-option':
            perfil(API)
            buy_trade_binary(API,horas,ativo,valor,direcao,timeM,gale,galex)
            op = input('Deseja fazer outra compra?[S/N]')
            while((op != 'S') and (op != 's') and (op != 'N') and (op != 'n')):
                print('Caractere inválido!')
                op = input('Deseja fazer outra compra?[S/N]')
            if op == 'N' or op  == 'n':
                cont += 1
                break
        elif pares == 'digital-option':
            perfil(API)
            buy_trade_digital(API,horas,ativo,valor,direcao,timeM,gale,galex)
            op = input('Deseja fazer outra compra?[S/N]')
            while((op != 'S') and (op != 's') and (op != 'N') and (op != 'n')):
                print('Caractere inválido!')
                op = input('Deseja fazer outra compra?[S/N]')
                if op == 'N' or op  == 'n':
                    cont += 1
                    break      
    loop = False
    return loop    

def paridades(API,timeframe):
    import time
    par = API.get_all_open_time() 
    def payout(par, tipo, timeframe):
        if tipo == 'turbo':
            a = API.get_all_profit()
            return int(100 * a[par]['turbo'])
        elif tipo == 'digital': 
            API.subscribe_strike_list(par, timeframe)
            while True:
                d = API.get_digital_current_profit(par, timeframe)
                if d != False:
                    d = int(d)
                    break
                time.sleep(1)
            API.unsubscribe_strike_list(par, timeframe)
            return d 
    print('\033[m\u001b[43;1mBINARY\033[m') 
    print('\033[m\u001b[42mATIVO\033[m  \033[m    \u001b[42mPAYOUT\033[m \u001b[32;1m')
    tipo = 'turbo'
    for paridade in par['turbo']:
        if par['turbo'][paridade]['open'] == True:
            print(paridade+'     '+str(payout(paridade, tipo, timeframe))+'%')
    print('\n')
    print('\033[m\u001b[43;1mDIGITAL\033[m') 
    print('\033[m\u001b[42mATIVO\033[m  \033[m    \u001b[42mPAYOUT\033[m \u001b[32;1m')
    tipo = 'digital'
    for paridade in par['digital']:
        if par['digital'][paridade]['open'] == True:
            print(paridade+'     '+str(payout(paridade,'digital', timeframe))+'%')

def dados_compra(at, horas, direcao, valor, gale,pares, timeM,galex):  
    import ativos, os
    paresl = 0
    import time
    while(paresl == 0):
        pares = input("Digite [1] para \033[m\u001b[43;1mBINARY\033[m \u001b[32;1mou [2] para \033[m\u001b[43;1mDIGITAL\033[m\u001b[32;1m=>")
        if(pares == '1'):
            pares = 'turbo-option'
            paresl += 1
        elif(pares == '2'):
            pares = 'digital-option' 
            paresl += 1
        else:
            print('Valor digitado incorretamente!') 
    print('#Você precisa digitar o horário no formato correto, caso contrário a ordem não será executada!') 
    print('#Exemplo de como digitar -> 00:00')       
    horas = input('Digite (horas:minutos)=>')
    while(paresl == 1): 
        print('#Digite o ativo como no exmplo abaixo!')
        print("#Exemplo -> EURUSD")                  
        at = input('Digite ativo=>')
        atv = ativos
        for i in atv.ACTIVES:
            if at != atv.ACTIVES[i]:
                msg = 'Ativo não encontrado'
            elif at == atv.ACTIVES[i]:
                msg = ''
                break
        if msg == 'Ativo não encontrado':
            print(msg)
        else:
            paresl += 1    
    while(paresl == 2):        
        timeM = int(input('Digite o timeframe [1] - [5] - [15]=>'))
        if timeM == 15 or timeM == 5 or timeM == 1:
            paresl += 1
        else:
            print('Timeframe digitado incorretamente!')  
    while(paresl == 3):        
        direcao = input('Digite [1] \033[m\u001b[42;1mCALL\033[m \u001b[32;1mou [2] para \033[m\u001b[41;1mPUT\033[m\u001b[32;1m=>')
        if(direcao == '1'):
            direcao = 'call'
            paresl += 1
        elif(direcao == '2'):
            direcao = 'put'   
            paresl +=1
        else:
            print('Direção digitada incorretamente!')      
    while(paresl == 4):
        try:               
            valor = float(input('Digite o valor=>'))
            paresl +=1
        except:
            print('Dados digitados incorretamente!')
    while(paresl == 5):
        try:            
            gale = int(input("Digite o quantos martingale=>"))
            if gale > 0:
                print('#Informe a baixo o fator multiplicação do gale!')
                ('#Exemplo: Seu valor de entra R$: 2, o fato mutiplicação: 1.3, o valor do proximo gale: 2.6')
                galex = float(input('Digite o fator multiplicação=>'))
            paresl +=1
        except:
            print('Dados digitados incorretamente!')    
    return at, horas, direcao, valor, gale,pares, timeM, galex
     

def resultado(API,pares,rest,ac,id):
    from config import resultados_trader
    dados = []
    control = 0
    if (pares == 'digital-option'):
        b = 'digital-option'
        from config import timestamp_converter
        status, historico = API.get_position_history_v2(pares, 10, 0, 0, 0)
        while(control == 0):
            for x in historico['positions']:
                status, historico = API.get_position_history_v2(pares, 10, 0, 0, 0)
                if str(id) == str(x['raw_event']['order_ids'][0]):
                    print('\u001b[32;1mPAR: '+str(x['raw_event']['instrument_underlying'])+' | '+' DIREÇÃO: '+str(x['raw_event']['instrument_dir'])+ ' | VALOR: '+str(x['invest']))
                    print('LUCRO: '+str(round(x['close_profit']-x['invest'],2))+' | INICIO OP: '+str(timestamp_converter(x['open_time']/1000, b))+' | FIM OP: '+str(timestamp_converter(x['close_time']/1000,b)))
                    ac = round(x['close_profit']-x['invest'],2)
                    if (int(x['close_profit']) <= 0):
                        rest = x['close_profit']-x['invest'] 
                        print('RESULTADO: \033[m\u001b[41;1mLOSS\033[m\u001b[32;1m')
                        t = 'LOSS'
                    elif(x['close_profit'] == x['invest']):
                        print('RESULTADO: -') 
                        t = '--'   
                    elif(x['close_profit'] > 0):
                        rest = x['close_profit']
                        print('RESULTADO:\033[m\u001b[42;1mWIN\033[m\u001b[32;1m')
                        t = 'WIN'          
                    dados = 'PAR:'+str(x['raw_event']['instrument_underlying'])+' | '+' DIREÇÃO: '+str(x['raw_event']['instrument_dir'])+ ' | VALOR: '+str(x['invest'])+'\n'+'LUCRO: '+str(round(x['close_profit']-x['invest'],2))+' | INICIO OP: '+str(timestamp_converter(x['open_time']/1000, b))+' | FIM OP: '+str(timestamp_converter(x['close_time']/1000,b)+'| RESULTADO:{}'.format(t))
                    resultados_trader(dados)
                    control += 1
                    check = False
                    break

    elif(pares == 'turbo-option'):
        b = 'turbo-option'
        from config import timestamp_converter
        status, historico = API.get_position_history_v2(pares , 10, 0, 0, 0)
        while(control == 0):
            for x in historico['positions']:
                status, historico = API.get_position_history_v2(pares , 10, 0, 0, 0)
                if str(id) == str(x['external_id']):
                    print('\u001b[32;1mPAR: '+str(x['raw_event']['active'])+' | '+' DIREÇÃO: '+str(x['raw_event']['direction'])+ ' | VALOR: '+str(x['invest']))
                    print('LUCRO: '+str(round(x['close_profit']-x['invest'],2))+' | INICIO OP: '+str(timestamp_converter((x['open_time']/1000),b))+' | FIM OP: '+str(timestamp_converter(x['close_time']/1000,b)))
                    ac = round(x['close_profit']-x['invest'],2)
                    if (x['close_profit'] <= 0):
                        rest = x['close_profit']-x['invest'] 
                        print('RESULTADO: \033[m\u001b[41;1mLOSS\033[m\u001b[32;1m')
                        t = 'LOSS'
                    elif(x['close_profit'] == x['invest']):
                        print('RESULTADO: -')    
                        t = '--'  
                    elif(x['close_profit'] > 0):
                        rest = x['close_profit']
                        print('RESULTADO:\033[m\u001b[42;1mWIN\033[m\u001b[32;1m') 
                        t = 'WIN'      
                    dados = 'PAR:'+str(x['raw_event']['instrument_underlying'])+' | '+' DIREÇÃO: '+str(x['raw_event']['instrument_dir'])+ ' | VALOR: '+str(x['invest'])+'\n'+'LUCRO: '+str(round(x['close_profit']-x['invest'],2))+' | INICIO OP: '+str(timestamp_converter(x['open_time']/1000, b))+' | FIM OP: '+str(timestamp_converter(x['close_time']/1000,b)+'| RESULTADO:{}'.format(t))
                    resultados_trader(dados)
                    control += 1
                    check = False
                    break
    return rest,ac

def buy_trade_digital(API,horas,at,valor,direcao,timeM,gale,galex):
    from config import get_time_now
    from datetime import datetime, timedelta
    import time, os
    tempo = timedelta()
    rest = 0
    contgale = 0
    ac = 0
    test = API.get_all_open_time()
    print('Inciando processo te automatização...')
    while True:   
        now = get_time_now(API)
        print(now.strftime("\r\u001b[32;1m%H:%M:%S"), end="", flush=True),
        if now.strftime('%H:%M:%S') == horas+':00':
            finsh = horas
            horas = ''
            status, id = API.buy_digital_spot(at,valor,direcao,timeM)
            if status:
                finsh = ''
                print('{} => Compra realizada, id de abertura:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),id))
                now = get_time_now(API)
                if (timeM == 1):
                    tempo = timedelta(seconds=60)
                elif(timeM == 2):
                    tempo = timedelta(seconds=300)   
                elif(timeM == 15):
                    tempo = timedelta(seconds=900)  
            if test['digital'][at]['open'] == False:
                print('{} => O ativo ' + at + ' esta fechado no momento.'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))) 
                break
            elif(finsh != ''):
                print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))    
                break    
        tempo = tempo - timedelta(seconds=1)
        if (tempo == timedelta(seconds=0)):
            pares = 'digital-option'
            print('{} => Aguardando resultado...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
            result = resultado(API,pares,rest,ac,id)
            time.sleep(1)
            if result <= 0:
                if gale != 0:
                    contgale += 1
                    print('Gale {}'.format(contgale))
                    valor = valor * galex
                    status, id  = API.buy_digital_spot(at,valor,direcao,timeM)
                    gale -= 1
                    if status:
                        finsh = 'a'
                        if finsh == 'a':
                            print('{} => Compra realizada, id de abertura:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),id))
                            if (timeM == 1):
                                tempo = timedelta(seconds=60)
                            elif(timeM == 2):
                                    tempo = timedelta(seconds=300)   
                            elif(timeM == 15):
                                tempo = timedelta(seconds=900)  
                            else:  
                                break
                    else:
                        print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))) 
                        break
            else:
                break
        print("\r", end="", flush=True),
        time.sleep(1)

def buy_trade_binary(API,horas,at,valor,direcao,timeM,gale,galex):
    from config import get_time_now
    from datetime import datetime, timedelta
    import time, os
    tempo = timedelta()
    rest = 0
    ac = 0
    contgale = 0
    test = API.get_all_open_time()
    print('Iniciando processo de automatização...')
    while True:   
        now = get_time_now(API)
        print (now.strftime("\r\u001b[32;1m%H:%M:%S"), end="", flush=True),
        if now.strftime('%H:%M:%S') == horas+':00':
            finsh = horas
            horas = ''
            status, id = API.buy(valor,at,direcao,timeM)
            if status:
                finsh = ''
                print('{} => Compra realizada, id de abertura:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),id))
                now = get_time_now(API)
                if (timeM == 1):
                    tempo = timedelta(seconds=60)
                elif(timeM == 2):
                    tempo = timedelta(seconds=300)   
                elif(timeM == 15):
                    tempo = timedelta(seconds=900)  
            if test['digital'][at]['open'] == False:
                print('{} => O ativo ' + at + ' esta fechado no momento.'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))) 
                break
            elif(horas != ''):
                print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))) 
                break    
        tempo = tempo - timedelta(seconds=1)
        if (tempo == timedelta(seconds=0)):
            pares = 'turbo-option'
            print('{} => Aguardando resultado...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
            result = resultado(API,pares,rest, ac, id)
            time.sleep(1)
            if result <= 0:
                if gale != 0:
                    contgale += 1
                    print('Gale {}'.format(contgale))
                    valor = valor * galex
                    status, id  = API.buy(at,valor,direcao,timeM)
                    gale -= 1
                    if status:
                        finsh = 'a'
                        now = get_time_now(API)
                        if finsh == 'a':
                            print('{} => Compra realizada, id de abertura:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),id))
                            if (timeM == 1):
                                tempo = timedelta(seconds=60)
                            elif(timeM == 2):
                                    tempo = timedelta(seconds=300)   
                            elif(timeM == 15):
                                tempo = timedelta(seconds=900)  
                            else:  
                                break  
                    else:
                        print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))) 
                        break        
            else:
                break
        print("\r", end="", flush=True),
        time.sleep(1)        

def painel_config():
    print('=========================================================================================')
    print('                                     Configurações')
    print('=========================================================================================')
    print('#Esconlha uma das opções a abaixo para ajustar as configurações:\n')
    print('[1] - {Binary|Digital}    [2] - {StopWin|StopLoss}    [3] - {Martigale}   [4] - {Voltar}\n')

def binary_digital():
    print('=========================================================================================')
    print('                                   Binary|Digital')
    print('=========================================================================================')

def stop_profit():
    print('=========================================================================================')
    print('                                Stop Win | Stop Loss')
    print('=========================================================================================')   

def martigale():
    print('=========================================================================================')
    print('                                      Martingale')
    print('=========================================================================================')         

def config(API,pares,stopW,stopL,galex,Phome):
    import os
    Phome = True
    while(Phome):
        try:
            perfil(API)
            painel_config()
            op = int(input('=>'))
            if op == 1:
                P = True
                while(P):
                    perfil(API)
                    binary_digital()
                    print('Escolha qual paridade deseja utilizar:\n')
                    print('Digite [B] para Binary ou [D] para Digital')
                    opc = input('=>')
                    while((opc != 'B') and (opc != 'b') and (opc != 'D') and (opc != 'd')):
                        perfil(API)
                        binary_digital()
                        print('Comando inválido!')
                        print('Escolha qual paridade deseja utilizar:\n')
                        print('Digite [B] para Binary ou [D] para Digital')
                        opc = input('=>')
                    if opc == 'B' or opc  == 'b':
                        pares = "turbo-option"
                        perfil(API)
                        binary_digital()
                        print('')
                        print('A opção Binary foi escolhida, aperte enter para voltar a configurações!')
                        xd = input()
                        op = ''
                        break
                    elif opc == 'D' or opc == 'd':
                        pares = "digital-option"
                        perfil(API)
                        binary_digital()
                        print('')
                        print('A opção Digital foi escolhida, aperte enter para voltar as configurações!')
                        xd = input()
                        op = ''
                        break
                    P = False
                    break
            elif op == 2:
                P = True
                while(P):
                    try:
                        perfil(API)
                        stop_profit()
                        print('')
                        print('#Por padrão o Stop Win esta em 2% e o Stop Loss em 4%!')
                        print('#Digite apenas os numeros, sem a "%"')
                        print('Defina os valores de Stop Win/Stop Loss abaixo:')
                        stopW = int(input('Stop Win =>'))
                        stopL = int(input('Stop Loss =>'))
                        perfil(API)
                        stop_profit()
                        print('')
                        print('Stop Win definido em {}%\n'.format(stopW))
                        print('Stop Loss definido em {}%'.format(stopL))
                        print('Aperte enter para voltar as configurações!')
                        xd = input()
                        op = 4
                        break
                    except:
                        perfil(API)
                        stop_profit()
                        print('Caractere inválido!')
                        print('#Por padrão o Stop Win esta em 2% e o Stop Loss em 4%!')
                        print('#Digite apenas os numeros, sem a "%"')
                        print('Defina os valores de Stop Win/Stop Loss abaixo:')
                        stopW = int(input('Stop Win =>'))
                        stopL = int(input('Stop Loss =>'))
                        perfil(API)
                        stop_profit()
                        print('')
                        print('Stop Win definido em {}%\n'.format(stopW))
                        print('Stop Loss definido em {}&'.format(stopL))
                        print('Aperte enter para voltar as configurações!')
                        xd = input()
                        op = 4
                        break 
                    P = False
                    break
            elif op == 3:
                try:
                    perfil(API)
                    martigale()
                    print('#Por padrão o fator Martingale é de 1.5 para a próxima entrada!\n')
                    galex = float(('Qual fator você deseja colocar =>'))
                    perfil(API)
                    martigale()
                    xd = input('Martingale configurado com sucesso, aperte enter para voltar!')
                    op = 4
                    P = False
                except:
                    perfil(API)
                    martigale()
                    print('#Por padrão o fator Martigale é de 1.5 para a próxima entrada!\n')
                    print('Valor digitou valou errado!')
                    galex = float(('Qual fator você deseja colocar =>'))
                    perfil(API)
                    martigale()
                    xd = input('Martigale configurado com sucesso, aperte enter para voltar!')
                    op = 4
                    P = False         
            elif op == 4:    
                Phome = False
                break
        except:
            continue
    return pares, stopW, stopL, galex,Phome 

def painel_lista():
    print('=========================================================================================')
    print('                                L0k1 Bot Ativo')
    print('=========================================================================================') 

def leitor_list():
    arq = open('lista.txt', 'r')
    dados = arq.readlines()
    arq.close()
    gaveta = []
    for i in dados:
        lista = i.split()
        if len(lista) == 0:
            del lista
        else:    
            gaveta.append(lista)  
    return gaveta


def ordens():
    from config import get_time_now
    ordens = []
    dados = leitor_list()
    j = len(dados)
    for i in range(j):
        receptor = dados[i][0]
        control = receptor.split(',')
        data = control[0]
        hora = control[1]
        Atv = control[2]
        Direc = control[3]  
        if Direc == 'CALL':
            Direc = 'call'
        elif Direc == 'PUT':
            Direc = 'put'  
        Tm = control[4].split('M')
        Tm = int(Tm[0])
        G = control[5].split('G')
        G = int(G[0])
        Vlr = control[6].split("$")
        Vlr = int(Vlr[0])
        Dic = {'key': '', 'Data' : data, 'HoraI': hora+':00','HoraF': '', 'HoraExe': '','Ativo' : Atv, 'Direcao': Direc, 
               'Timeframe': Tm, 'Gale': G, 'Valor': Vlr, 'ContaGale': 0} 
        ordens.append(Dic)
    return ordens            

def painel_automatizador(API,stopW,stopL,pares,galex,loop):
    import os
    from config import get_time_now
    import time
    from datetime import datetime, timedelta
    tempo = timedelta()
    rest = 0
    contgale = 0
    test = API.get_all_open_time()
    now = get_time_now(API)
    loop = True
    while(loop):
        banner2()
        print('')
        print('################################\033[m\u001b[41;1m A T E N Ç Ã O \033[m\u001b[32;1m##########################################\n')
        print('Por padrão a paridade utilizada no sistema é \033[m\u001b[43;1mDIGITAL\033[m\u001b[32;1m')
        if pares == 'digital-option':
            ps = 'Digital'
        else:
            ps = 'Binary'    
        print('A paridade que você esta utilizando é: {}'.format(ps))
        print('Seu saldo atual é: {}'.format(API.get_balance()))
        print('Stop Win: {}%'.format(stopW))
        print('Stop Loss: {}%'.format(stopL))
        print('Martingale está definido em: {}'.format(galex))
        print('Caso deseje alterar vá em configurações!')
        print('Deseja continuar?[S/N]')
        op = input('=>')
        while((op != 'S') and (op != 's') and (op != 'N') and (op != 'n')):
            banner2()
            print('')
            print('################################\033[m\u001b[41;1m A T E N Ç Ã O \033[m\u001b[32;1m##########################################\n')
            print('Por padrão a paridade utilizada no sistema é \033[m\u001b[43;1mDIGITAL\033[m\u001b[32;1m')
            if pares == 'digital-option':
                p = 'Digital'
            elif pares == 'turbo-option':
                p = 'Binary'
            print('A paridade que você esta utilizando é: {}'.format(p))
            print('Seu saldo atual é: {}'.format(API.get_balance()))
            print('Stop Win: {}%'.format(stopW))
            print('Stop Loss: {}%'.format(stopL))
            print('Caso deseje alterar vá em configurações!')
            print('Caractere inválido!!!')
            print('Deseja continuar?[S/N]')
            op = input('=>')
        if op == 'N' or op == 'n':
            loop = False
            break
        elif op == 'S' or op == 's':
            while True:
                banner2()
                painel_lista()
                if pares == 'digital-option':
                    automatizador_digital(API,pares,stopW,stopL,galex)
                elif pares == 'turbo-option':
                    automatizador_binary(API,pares,stopW,stopL,galex)
    return loop                


       
def automatizador_digital(API,pares,stopW,stopL,galex):
    from config import get_time_now, resultados_trader
    from datetime import datetime, timedelta
    import time
    test = API.get_all_open_time()
    check = []
    checkgale = []
    ac = 0
    rest = 0
    banca = API.get_balance()
    stopWI = stopW/100
    stopWI = round(int(API.get_balance())*stopWI,2)
    Win = round(int(API.get_balance()) + stopWI,2)
    stopLI = stopL/100
    stopLI = round(int(API.get_balance())*stopLI,2)
    Loss = round(int(API.get_balance()) - stopLI,2)
    saldo = 0
    exe = ordens()
    N = len(exe)
    indice = []
    for i in range(N):
        exe[i]['HoraExe'] = datetime.strptime(exe[i]['Data']+' '+exe[i]['HoraI'],'%Y/%m/%d %H:%M:%S') - timedelta(seconds=2)
    while(Win > banca or Loss < banca):
        now = get_time_now(API)
        print (now.strftime("\r\u001b[32;1m%H:%M:%S"), end="", flush=True),
        for i in range(N):
            try:  
                now = get_time_now(API)   
                if check != []:
                    if now.strftime('%Y-%m-%d %H:%M:%S') == str(exe[i]['HoraF']):
                        while check != []:
                            print('{} => Aguardando resultado...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                            id = check[0]['id']
                            try:
                                result,ac = resultado(API,pares, rest,ac,id)
                                saldo += ac
                                print('{} => Saldo atual:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),saldo))
                            except:
                                print('{} => Ocorreu algum erro no carregamento do resultado, ordem Martingale cancelada!'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))  
                                check.pop[0]  
                                print('Sistema reiniciado...')
                            if result <= 0:
                                for i in range(N):
                                    if check[0]['indice'] == i:
                                        if exe[i]['Gale'] != 0:
                                            exe[i]['ContaGale'] = exe[i]['ContaGale'] + 1
                                            print('{} => Martingale {} da compra programada no horario:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['ContaGale'],exe[i]['HoraI']))
                                            dados = '{} => Martingale {} da compra programada no horario:{}'.format(now.strftime("%H:%M:%S"),exe[i]['ContaGale'],exe[i]['HoraI'])
                                            resultados_trader(dados)
                                            exe[i]['Valor'] = int(exe[i]['Valor']) * galex
                                            status, id = API.buy_digital_spot(str(exe[i]['Ativo']),exe[i]['Valor'],str(exe[i]['Direcao']),exe[i]['Timeframe'])
                                            check_info = {'id': id, 'indice': i}
                                            checkgale.append(check_info)
                                            exe[i]['Gale'] = int(exe[i]['Gale']) - 1
                                            if status:
                                                now = get_time_now(API)
                                                print('{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id))
                                                dados = '{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id)
                                                resultados_trader(dados)
                                                if exe[i]['Timeframe'] == 1:
                                                    exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=60) 
                                                    print(exe[i]['TimeFrame'])  
                                                elif exe[i]['Timeframe'] == 5:
                                                    exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=300)   
                                                elif exe[i]['Timeframe'] == 15:
                                                    exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=900)   
                                            else:
                                                print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                                                dados = '{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("%H:%M:%S"))
                                                resultados_trader(dados)
                            check.pop(0)
                        try:
                            while checkgale != []:
                                x = checkgale[0]
                                check.append(x) 
                                checkgale.pop(0)
                        except:
                            continue        
                if now.strftime('%Y-%m-%d %H:%M:%S') == str(exe[i]['HoraExe']):
                    Atv = exe[i]['Ativo']
                    if test['digital'][Atv]['open'] == False:
                            print('{} => O ativo ' + Atv + ' esta fechado no momento.'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                            dados = '{} => O ativo ' + Atv + ' esta fechado no momento.'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))
                            resultados_trader(dados)
                    status, id = API.buy_digital_spot(str(exe[i]['Ativo']),exe[i]['Valor'],str(exe[i]['Direcao']),exe[i]['Timeframe'])
                    check_info = {'id': id, 'indice': i, 'HoraG': ''}
                    check.append(check_info)
                    if status:
                        print('{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id))
                        dados = '{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id)
                        resultados_trader(dados)
                        if exe[i]['Timeframe'] == 1:
                            exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=60)   
                            exe[i]['Key'] = id
                        elif exe[i]['Timeframe'] == 5:
                            exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=300)   
                            exe[i]['Key'] = id
                        elif exe[i]['Timeframe'] == 15:
                            exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=900)   
                            exe[i]['Key'] = id
                    else:
                            print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                            dados = '{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("%H:%M:%S"))
                            resultados_trader(dados)
            except:
                print('{} => Ocorreu algum erro no processameto...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
        print (now.strftime("\r\u001b[32;1m%H:%M:%S"), end="", flush=True),
        print("\r", end="", flush=True),
        time.sleep(1)
    if banca >= Win:
        now = get_time_now(API)
        print('{} => Stop Win atingido com sucesso, seu ganho de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo)) 
        dados = '{} => Stop Win atingido com sucesso, seu ganho de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo)
        resultados_trader(dados)
    elif banca <= Loss:
        now = get_time_now
        print('{} => Stop Loss atingido, sua perda de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo))    
        dados = '{} => Stop Loss atingido, sua perda de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo)
        resultados_trader(dados)
           


def automatizador_binary(API,pares,stopW,stopL,galex):
    from config import get_time_now, resultados_trader
    from datetime import datetime, timedelta
    import time
    test = API.get_all_open_time()
    check = []
    checkgale = []
    ac = 0
    rest = 0
    banca = API.get_balance()
    stopWI = stopW/100
    stopWI = round(int(API.get_balance())*stopWI,2)
    Win = round(int(API.get_balance()) + stopWI,2)
    stopLI = stopL/100
    stopLI = round(int(API.get_balance())*stopLI,2)
    Loss = round(int(API.get_balance()) - stopLI,2)
    saldo = 0
    exe = ordens()
    N = len(exe)
    indice = []
    for i in range(N):
        exe[i]['HoraExe'] = datetime.strptime(exe[i]['Data']+' '+exe[i]['HoraI'],'%Y/%m/%d %H:%M:%S') - timedelta(seconds=2)
    while(Win > banca or Loss < banca):
        now = get_time_now(API)
        print (now.strftime("\r\u001b[32;1m%H:%M:%S"), end="", flush=True),
        for i in range(N):
            now = get_time_now(API)
            if now.strftime('%Y-%m-%d %H:%M:%S') == str(exe[i]['HoraF']):
                while check != []:
                    print('{} => Aguardando resultado...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                    id = check[0]['id']
                    result,ac = resultado(API,pares, rest,ac,id)
                    saldo += ac
                    print('{} => Saldo atual:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),saldo))
                    if result <= 0:
                        for i in range(N):
                            if check[0]['indice'] == i:
                                if exe[i]['Gale'] != 0:
                                    exe[i]['ContaGale'] = exe[i]['ContaGale'] + 1
                                    print('{} => Martingale {} da compra programada no horario:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['ContaGale'],exe[i]['HoraI']))
                                    dados = '{} => Martingale {} da compra programada no horario:{}'.format(now.strftime("%H:%M:%S"),exe[i]['ContaGale'],exe[i]['HoraI'])
                                    resultados_trader(dados)
                                    exe[i]['Valor'] = int(exe[i]['Valor']) * galex
                                    status, id = API.buy(str(exe[i]['Valor']),exe[i]['Ativo'],str(exe[i]['Direcao']),exe[i]['Timeframe'])
                                    check_info = {'id': id, 'indice': i}
                                    checkgale.append(check_info)
                                    exe[i]['Gale'] = int(exe[i]['Gale']) - 1
                                    if status:
                                        now = get_time_now(API)
                                        print('{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id))
                                        dados = '{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id)
                                        resultados_trader(dados)
                                        if exe[i]['Timeframe'] == 1:
                                            exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=60)   
                                            exe[i]['Key'] = id
                                        elif exe[i]['Timeframe'] == 5:
                                            exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=300)   
                                            exe[i]['Key'] = id
                                        elif exe[i]['Timeframe'] == 15:
                                            exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=900)   
                                            exe[i]['Key'] = id
                                    else:
                                        print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                                        dados = '{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("%H:%M:%S"))
                                        resultados_trader(dados)
                    check.pop(0)
                try:
                    while checkgale != []:
                        x = checkgale[0]
                        check.append(x) 
                        checkgale.pop(0)
                except:
                    continue        
            if now.strftime('%Y-%m-%d %H:%M:%S') == str(exe[i]['HoraExe']):
                Atv = exe[i]['Ativo']
                if test['digital'][Atv]['open'] == False:
                        print('{} => O ativo ' + Atv + ' esta fechado no momento.'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                        dados = '{} => O ativo ' + Atv + ' esta fechado no momento.'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"))
                        resultados_trader(dados)
                status, id = API.buy(str(exe[i]['Valor']),exe[i]['Ativo'],str(exe[i]['Direcao']),exe[i]['Timeframe'])
                check_info = {'id': id, 'indice': i, 'HoraG': ''}
                check.append(check_info)
                if status:
                    print('{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("\r\u001b[32;1m%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id))
                    dados = '{} => Compra realizada: Ativo:{} - Direção:{} - Valor:{} - id da compra:{}'.format(now.strftime("%H:%M:%S"),exe[i]['Ativo'],exe[i]['Direcao'],exe[i]['Valor'],id)
                    resultados_trader(dados)
                    if exe[i]['Timeframe'] == 1:
                        exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=60)   
                        exe[i]['Key'] = id
                    elif exe[i]['Timeframe'] == 5:
                        exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=300)   
                        exe[i]['Key'] = id
                    elif exe[i]['Timeframe'] == 15:
                        exe[i]['HoraF'] = datetime.strptime(str(exe[i]['Data'])+' '+str(exe[i]['HoraI']),'%Y/%m/%d %H:%M:%S') + timedelta(seconds=900)   
                        exe[i]['Key'] = id
                else:
                        print('{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("\r\u001b[32;1m%H:%M:%S")))
                        dados = '{} => Ocorreu algum erro na abertura da compra...'.format(now.strftime("%H:%M:%S"))
                        resultados_trader(dados)
        print (now.strftime("\r\u001b[32;1m%H:%M:%S"), end="", flush=True),
        print("\r", end="", flush=True),
        time.sleep(1)        
    if banca >= Win:
        now = get_time_now(API)
        print('{} => Stop Win atingido com sucesso, seu ganho de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo)) 
        dados = '{} => Stop Win atingido com sucesso, seu ganho de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo)
        resultados_trader(dados)
    elif banca <= Loss:
        now = get_time_now
        print('{} => Stop Loss atingido, sua perda de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo))    
        dados = '{} => Stop Loss atingido, sua perda de hoje:{}'.format(now.strftime("%H:%M:%S"),saldo)
        resultados_trader(dados)    