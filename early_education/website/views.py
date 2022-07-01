
from django.shortcuts import render 
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Create your views here.
def reading(request):
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
            
        
        
        return render(request, 'reading.html', {'messageNames':messageNames, 'email': email, 'phone': phone, 'message':message})
        
    else:
        # return the page 
        return render(request, 'reading.html', {})

# Create your views here.
def math(request):
    return render(request, 'math.html', {})

# Create your views here.
def reading(request):
    return render(request, 'reading.html', {})

    # Create your views here.
def science(request):
    return render(request, 'science.html', {})

    # Create your views here.
def addition(request):
    return render(request, 'addition.html', {})    


