from django.shortcuts import redirect

def is_loged_in(function):
    def wrap(request, *args, **kwargs):
        if request.session.get('account_email',False):
            return redirect('sent:home')      
        else:
            return function(request, *args, **kwargs)
    return wrap

def is_loged_out(function):
    def wrap(request, *args, **kwargs):
        if request.session.get('account_email',False):
            return function(request, *args, **kwargs)       
        else:
             return redirect('client:login')   
    return wrap