from django.shortcuts import render,redirect
from .handler import ClientHandler
from script.client_session import SharedHadler
from script.decorator import is_loged_in

# Create your views here.

""" Client Logout """

def client_logout(request):
    shared = SharedHadler()
    request = shared.log_out(request)
    return redirect('client:login')

""" Client login  """
@is_loged_in
def client_login(request):
    hadler = ClientHandler()
    if request.method == "POST":
        hadler.setmessage = True
        request, success = hadler.account_login(request)
        if success: return redirect('chat:homepage')
    return render(request,'client/client_login.html',{})

""" Client Signup"""
@is_loged_in
def client_signup(request):
    hadler = ClientHandler()
    success = False
    if request.method == "POST":
        if request.POST['registor'] == "detail":
            user ,request = hadler.get_client(request)
            if not user:
                success = True
        else:
             hadler.setmessage = True
             request,err = hadler.account_create(request)
             if not err:
                 return redirect('client:login')
    return render(request,'client/client_signup.html',{'city':hadler.get_country(),'gender':hadler.get_gender(),'success':success})