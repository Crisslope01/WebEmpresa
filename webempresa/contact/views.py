from django.shortcuts import render, redirect 
from django.urls import reverse      # Para redireccionar a una URL
from django.core.mail import EmailMessage   # Para enviar el correo
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            # enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "6b55cb5017-4c0fc2+1@inbox.mailtrap.io",
                ["lopez.valenzuela.cristian@gmail.com"],   # Lista de correos
                reply_to=[email]
            )
            
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
        
    return render(request, "contact/contact.html", {'form':contact_form})
