from .models import Account,Myclient,CITY,GENDER
from django.contrib.auth.hashers import make_password, check_password
from script import client_session
class ClientHandler:
    def __init__(self) -> None:
        self.setmessage = False
        self.clienthandler = client_session.SharedHadler()
    
    # change to dictionay value
    def get_country(self):
         city = []
         for value in CITY:
              city.append({'value': value[0], 'name':value[1]})
         return city

    # change to gender to dictionary value
    def get_gender(self):
         gender = []
         for value in GENDER:
              gender.append({'value': value[0], 'name':value[1]})
         return gender

    # get all recorded client created accounts
    def get_all_account(self):
        return Myclient.objects.all()
    
    # get single client
    def get_client(self,request):
        try:
            _ = Myclient.objects.get(email=request.POST["email"])
            if self.setmessage: 
                     request = self.clienthandler.set_message('success', "Email Found", request)
                     self.setmessage = False
            return True , request
        except Exception as e:
             if self.setmessage: 
                   request = self.clienthandler.set_message('error', e, request)
                   self.setmessage = False
             return False ,request
        
    # create new account   
    def account_create(self,request):
         success = False 
         try:
               client = Myclient(
                first_name = request.POST["first_name"],
                middle_name = request.POST["middle_name"],
                last_name = request.POST["last_name"],
                phone = request.POST["phone"],
                phoneb = request.POST["phoneb"],
                email = request.POST["email"],
                gender=request.POST["gender"],
                coutry  = request.POST["coutry"]
               )
               if request.POST['password'] == request.POST['passwordcon']:
                    client.save()
                    account = Account(user = client,password = make_password(request.POST['password']))
                    account.save()
                    if self.setmessage: 
                         request = self.clienthandler.set_message('success', "Account Created", request)
                         self.setmessage = False
               else:
                     success = True
                     if self.setmessage: 
                         request = self.clienthandler.set_message('warning', "Password do not match", request)
                         self.setmessage = False                   
               return request, success
         except Exception as e:
             if self.setmessage: 
                     request = self.clienthandler.set_message('error', e, request)
                     self.setmessage = False
             return request, True
     
    # login conform for client
    def account_login(self,request):
         success = False
         
         try:   
               client = Account.objects.get(user__email=request.POST["email"])
               if check_password(request.POST['password'],client.password):
                    success = True
                    if self.setmessage: 
                         request.session['account_email'] = request.POST["email"]
                         request.session['full_name'] = f"{client.user.first_name} {client.user.middle_name} {client.user.last_name}"
                         request = self.clienthandler.set_message('success', " Welcome", request)
                         self.setmessage = False 
               else:
                    if self.setmessage: 
                         request = self.clienthandler.set_message('info', "Password do not match", request)
                         self.setmessage = False 
               return request, success
         except Exception as e:
             if self.setmessage: 
                     request = self.clienthandler.set_message('error', e, request)
                     self.setmessage = False
             return request, False