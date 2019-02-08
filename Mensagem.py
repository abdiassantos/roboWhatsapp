from twilio.rest import Client
 
class Mensagem(object):
    

    def enviarMensagem(fromNumber, toNumber, bodyMessage):
        account_sid = 'ACe26741c00ee81a87bafd30930c7765a1' 
        auth_token = '35c7a673b6724e04cc8d22b7a1afe37c'

        client = Client(account_sid, auth_token) 
 
        message = client.messages.create(
         from_ = fromNumber,
         body = bodyMessage,
         to = toNumber
        )
 
        print(message.sid)
    