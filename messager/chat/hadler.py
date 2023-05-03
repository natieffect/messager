from script.client_session import SharedHadler
from django.db.models import Q 
from client.models import Account
from .models import Message
from script import client_session

class ChatHandler:
    def __init__(self) -> None:
        self.setmessage = False
        self.clienthandler = client_session.SharedHadler()

    # get recorded account 
    def getAccounts(self):
        accounts = Account.objects.all()
        return accounts

    # get client sent message
    def get_sent_Message(self,request):
        try:
            resiver = Account.objects.get(id=request.POST["sendto"])
            sender  = Account.objects.get(user__email = request.session.get('account_email',False))
            message_all = Message.objects.filter(Q(send_to =resiver, send_from = sender)|Q(send_to =sender, send_from = resiver)).order_by('pub_date')
            return message_all,resiver,request
        except Exception as e:
             if self.setmessage: 
                   request = self.clienthandler.set_message('error', f"{e} from list", request)
             return False ,False,request
        
    #send new message to client
    def send_message(self,request):
        try:
            message_send = Message.objects.create( 
                send_to = Account.objects.get(id=request.POST["sendto"]),
                send_from = Account.objects.get(user__email =request.POST["sender"]),
                detail = request.POST['detail']
            )
            message_send.save()
            if self.setmessage:
                 request = self.clienthandler.set_message('success', "message is sent", request)
            return request,message_send
        except Exception as e:
             if self.setmessage: 
                   request = self.clienthandler.set_message('error', e, request)
             return request,False
        
    # Delete client message
    def delete_message(self,request):
        try:
             sentMessage = Message.objects.get(id= request.POST['deleteid'])
             sentMessage.delete()
             if self.setmessage: 
                   request = self.clienthandler.set_message('success', 'message deleted', request)
             return request,True            
        except Exception as e:
             if self.setmessage: 
                   request = self.clienthandler.set_message('error', e, request)
             return request,False

    # update client sent message
    def edit_message(self,request):
        try:
             sentMessage = Message.objects.get(id= request.POST['editid'])
             sentMessage.update(detail= request.POST['detail'])
             if self.setmessage: 
                   request = self.clienthandler.set_message('success', 'message edited', request)
             return request,True            
        except Exception as e:
             if self.setmessage: 
                   request = self.clienthandler.set_message('error', e, request)
             return request,False