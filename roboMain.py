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
indiceLoop = 0
tempoDecorrido = 0
executando = True
while executando == True:
        ##inicia o Loop até que se complete o total de tempo determinado
        while int(now.hour) >= 9 and int(now.hour) < 10 and int(now.minute) >= 0 and int(now.minute) < 59:
            # for x in range(len(listaDeTelefones)): 
            #     EnviarMensagem.enviarMensagem('whatsapp:+14155238886',
            #     'whatsapp:{}'.format(listaDeTelefones[x]),
            #     'Teste de Tempo')
            Mensagem.enviarMensagem('whatsapp:+14155238886',
                'whatsapp:{}'.format(listaDeTelefones[0]),
                'Tempo decorrido entre cada mensagem: {} Minutos'.format(tempoDecorrido))
            tempoDecorrido += 10
            sleep(600)
            # indiceLoop += 1
            
            ##Parar o Loop
            if int(now.hour) == 9 and int(now.minute) == 59:
                executando = False

            

#%%
# from datetime import datetime
# now = datetime.now()
# if int(now.hour) == 9 and int(now.minute) == 5:
#     while int(now.hour) != 9 and int(now.minute) != 14:
#         print('funcionou')

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