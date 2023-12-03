from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import ContactForm
from .models import Contact, SocialMedia

def contact(request):

    contact = Contact.objects.first()
    form = ContactForm()
    social = SocialMedia.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been accepted, we will contact you soon')
            return redirect("contact")
    context = {
        'contact': contact,
        'form': form,
        'social': social
    }

    return render(request, 'contact/contact.html', context)