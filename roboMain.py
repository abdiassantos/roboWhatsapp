from time import sleep
from Mensagem import *
from datetime import datetime


##Declaração de variáveis.
listaDeTelefones = [
    '+558699685966', ##Abdias Vivo 0
    '+558699491221', ##Alvaro 1
    '+558688676906', ##Kássio 2
    '+558699111960', ##Luiza 3
    '+558699037002', ##Marquinhos 4
    '+558695354927', ##Brasil 5
    '+558699463489', ##Jaime 6
    '+558688156192', ##Carlito 7
    '+558699677811', ##Abdias Tim 8
    '+558688272410' ##Zé Maria 9
]
now = datetime.now()
dataAtual = now.strftime('%d/%m/%Y')
indiceLoop = 1
tempoDecorrido = 0



for x in range(len(listaDeTelefones)): 
    Mensagem.enviarMensagem('whatsapp:+14155238886',
    'whatsapp:{}'.format(listaDeTelefones[x]),
    'Senhores, Iniciando Contagem do Robo de envios pelo Whatsapp, Para não atrapalhar, silencie este chat')
    print('-=' * 30)

while dataAtual != '10/02/2019':

    now = datetime.now()
    horaAtual = now.strftime('%H:%M')
    dataAtual = now.strftime('%d/%m/%Y')

    ##inicia o Loop até que se complete o total de tempo determinado
    if horaAtual >= '08:00' and horaAtual < '22:00':
        for x in range(len(listaDeTelefones)): 
            Mensagem.enviarMensagem('whatsapp:+14155238886',
            'whatsapp:{}'.format(listaDeTelefones[x]),
            'Mensagem: {} - Tempo decorrido entre cada mensagem: {} Minutos'.format(indiceLoop, tempoDecorrido))
            
        # Mensagem.enviarMensagem('whatsapp:+14155238886',
        #     'whatsapp:{}'.format(listaDeTelefones[0]),
        #     'Mensagem: {} - Tempo decorrido entre cada mensagem: {} Minutos'.format(indiceLoop, tempoDecorrido))
        tempoDecorrido += 10
        sleep(600)
        indiceLoop += 1
        print('-=' * 30)

            

# #%%
# from datetime import datetime
# now = datetime.now()
# horaAtual = now.strftime('%H:%M')
# if horaAtual >= '10:36':
#         print('funcionou')
# else:
#     print('Não funcionou')

# from twilio.rest import Client

# account_sid = 'ACe26741c00ee81a87bafd30930c7765a1' 
# auth_token = '35c7a673b6724e04cc8d22b7a1afe37c'

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+558699685966'
#                           )

# print(message.sid)