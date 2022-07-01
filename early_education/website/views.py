
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

        
def addition(request): # backend ADDITION PAGE
	# generate random numbers whole numbers frm python
	from random import randint

	# create variables
	num_1 = randint(0,10)
	num_2 = randint(0,10)

	# IF REQUEST METHOD IS A POST 
	if request.method == "POST":
		# GRAB IN THE FORM AND STICK IN VARIABLE
		answer = request.POST['answer']
		# pass num1 and num2 from frontend
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']
		# error handling if the answer is empty
		if not answer:
			my_answer = "Please try again! "
			color = 'warning'
			return render(request, 'addition.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			}) 

		# comparision code / determine correct answer 
		correct_answer = int(old_num_1) + int(old_num_2)
		if int (answer) == correct_answer:
			my_answer = "Correct!  " + old_num_1 + " + " + old_num_2 + " = " + answer
			color = "success " # color of the pop up box from boostrap
		else:
			my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger " # color of the pop up box from boostrap

		# CONTEXT DICTIONARY returns to the screen 
		return render(request, 'addition.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color, # pass in color for pop up box 
			}) 
	# initial start 
	return render(request,'addition.html', {
			'num_1': num_1,
			'num_2': num_2,
			})     

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


