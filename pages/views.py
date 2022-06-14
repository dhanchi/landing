from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

# def about(request):
#     return render(request, 'index.html')

# def contact(request):
#     form = contactForm()
#     context = {
#         'form':form,
#     }
#     return render(request, "contact.html", context)