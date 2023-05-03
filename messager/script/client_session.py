from django.contrib import messages

class SharedHadler:
    def __init__(self) -> None:
         self.setmessage = False

    # set message to request value
    def set_message(self, type, msg, request):
        if type == 'success':
             messages.add_message(request, messages.SUCCESS, msg)
        elif type == 'info':
             messages.add_message(request, messages.INFO, msg)
        elif type == 'warning':
             messages.add_message(request, messages.WARNING, msg)
        else:
             messages.add_message(request, messages.ERROR, msg)
        self.setmessage = False
        return request

    # Create your views here.
    def log_out(self,request):
        for key in list(request.session.keys()):
            del request.session[key]
        return request