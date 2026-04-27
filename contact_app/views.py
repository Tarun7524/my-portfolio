from django.shortcuts import render
from .models import ContactMessage

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save to SQL database
        ContactMessage.objects.create(name=name, email=email, message=message)
        
        # Optional: Add a success message
        return render(request, 'index.html', {'status': 'success'})
        
    return render(request, 'index.html')
