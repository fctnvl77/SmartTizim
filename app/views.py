from django.shortcuts import render

# Create your views here.


from django.views.generic import ListView
from .models import *
from django.core.mail import send_mail,EmailMultiAlternatives
def homePage(request):
    subject='Testing Mail'
    form_email = 'fctnvlfc06@gmail.com'
    msg='<p>Xush kelibsiz<p/>'
    to ='fctnvlwind@gmail.com'
    msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    msg.content_subtype='html'
    msg.send()

def index(request):
    tarif = Tarif.objects.all()
    jamoa = Jamoa.objects.all()
    xizmatlar = Xizmatlar.objects.all()
    xususiyat = Xususiyat.objects.all()
    boglanish = Boglanish.objects.all()
    statistika = Statistika.objects.all()
    asosiy_rasm = Asosiy_rasm.objects.all()
    malumot = Malumot.objects.all()
    contex = {
        'Asosiy_rasm':asosiy_rasm,
        'Jamoa':jamoa,
        'Tarif':tarif,
        'Xizmatlar':xizmatlar,
        'Xususiyat':xususiyat,
        'Boglanish':boglanish,
        'Statistika':statistika,
        'Malumot':malumot,
    }
    return render(request, ['index.html', 'xususiyat.html'], contex)

