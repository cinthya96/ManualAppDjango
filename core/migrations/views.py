from django.shortcuts import render

def home(request, plantilla="home.htlm"):
    return render(request, plantilla)

def about(request, plantilla="about.htlm"):
    return render(request, plantilla)

def contact(request, plantilla="contact.htlm"):
    return render(request, plantilla)


