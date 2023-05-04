from django.shortcuts import render
from . import hadler
from django.http import JsonResponse
from script.decorator import is_loged_out
# Create your views here.

""" chat home page for user"""
@is_loged_out
def chat_homepage(request):
    hadle = hadler.ChatHandler()
    context = {}
    if request.method == "POST":
        hadle.setmessage = False
        if request.POST['action']=="sendmessage":
            #hadle.setmessage = True
            request,client = hadle.send_message(request)
            data = {'firstName':client.send_from.user.first_name, 
                    'lastName':client.send_from.user.last_name,
                    'pubDate':client.pub_date,
                    'detail':client.detail,
                    'iD':f"{client.id}"}
            return JsonResponse(data)

        message,resiver,request =hadle.get_sent_Message(request)
        if message:
            context.update(
                {"messagefound":True}
            )
            context.update({"message_all":message,"resiver":resiver})
    else:
        account = hadle.getAccounts()
        context = {'list_val':account}
    return render(request,'chat/chat_homepage.html',context)

"""client delete message"""
def chat_deletemessage(request):
    hadle = hadler.ChatHandler()
    if request.method == "POST":
        hadle.setmessage = False
        request, success = hadle.delete_message(request)
        data = {'success': success}
        return JsonResponse(data)

"""update delete message"""
def chat_updatemessage(request):
    hadle = hadler.ChatHandler()
    if request.method == "POST":
        request, success = hadle.edit_message(request)
        data = {'success': success}
        return JsonResponse(data)