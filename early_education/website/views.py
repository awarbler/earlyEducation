import imp
from django.shortcuts import render 
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Create your views here.
def contact(request):
    # pass in 
    if request.method == "POST":
        messageNames = request.POST['messageNames']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # send email 
        send_mail(
            #subjct
            messageNames,
            #message
            message,
            # from email
            email,
            # to email
            ['txwarbler@gmail.com'],
            fail_silently= False,
        )
            
        
        
        return render(request, 'contact.html', {'messageNames':messageNames, 'email': email, 'phone': phone, 'message':message})
        
    else:
        # return the page 
        return render(request, 'contact.html', {})

# Create your views here.
def math(request):
    return render(request, 'math.html', {})

# Create your views here.
def contact(request):
    return render(request, 'contact.html', {})

    # Create your views here.
def about(request):
    return render(request, 'about.html', {})

    # Create your views here.
def why(request):
    return render(request, 'why.html', {})    


