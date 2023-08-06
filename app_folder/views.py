from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        '''
        send_mail(
           'message from ' + name, #Subject
            message, # message
            subject, # subject
            email, # from email
           ['temitopeayobami995@gmail.com'], # to email
        )
        '''
        send_mail(name, message, subject, email, ['temitopeayobami995@gmail.com'])
        return render(request, 'apps/home.html', {'name':name})
    
    else:
        return render(request, 'apps/home.html', {})
        
