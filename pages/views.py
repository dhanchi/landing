from django.shortcuts import render, redirect
from  home import settings
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError



def home(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                    'name': form.cleaned_data['name'], 
                    'subject': form.cleaned_data['subject'], 
                    'email': form.cleaned_data['email'], 
                    'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            sender = form.cleaned_data['email']
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject'], 
            msg = f"""Sender: {name}<{sender}>,
                      subject': {subject}, 
                    Message: {body.get('message')}"""
            
            send_mail(subject=body.get('subject').strip(),message=msg, from_email=body.get('email'), recipient_list=['dhanchillc@gmail.com'] ) 
            return redirect ("success")
    form = ContactForm()
    return render(request, 'index.html', {'form':form})

def success(request):
    return render(request, 'contact.html')
