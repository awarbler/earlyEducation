
from django.shortcuts import render 

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# Create your views here.

       
def addition(request): # backend ADDITION PAGE
	# generate random numbers whole numbers frm python
	from random import randint

	# create variables
	num_1 = randint(0,9)
	num_2 = randint(0,9)

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

def subtraction(request):
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
			return render(request, 'division.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			}) 

		# comparision code / determine correct answer 
		correct_answer = int(old_num_1) - int(old_num_2)
		if int (answer) == correct_answer:
			my_answer = "Correct!  " + old_num_1 + " - " + old_num_2 + " = " + answer
			color = "success " # color of the pop up box from boostrap
		else:
			my_answer = "Incorrect! " + old_num_1 + " - " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger " # color of the pop up box from boostrap

		# CONTEXT DICTIONARY returns to the screen 
		return render(request, 'subtraction.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color, # pass in color for pop up box 
			}) 
	# initial start 
	return render(request,'subtraction.html', {
			'num_1': num_1,
			'num_2': num_2,
			})   
def multiplication(request):
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
			return render(request, 'division.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color,
			}) 

		# comparision code / determine correct answer 
		correct_answer = int(old_num_1) * int(old_num_2)
		if int (answer) == correct_answer:
			my_answer = "Correct!  " + old_num_1 + " x " + old_num_2 + " = " + answer
			color = "success " # color of the pop up box from boostrap
		else:
			my_answer = "Incorrect! " + old_num_1 + " x " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger " # color of the pop up box from boostrap

		# CONTEXT DICTIONARY returns to the screen 
		return render(request, 'multiplication.html', {
			'answer':answer,
			'my_answer':my_answer,
			'num_1': num_1,
			'num_2': num_2,
			'color': color, # pass in color for pop up box 
			}) 
	# initial start 
	return render(request,'multiplication.html', {
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

  


