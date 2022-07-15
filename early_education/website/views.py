
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
			return render(request, 'subtraction.html', {
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
			return render(request, 'multiplication.html', {
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

	# define spelling list
	spelling_list = [
		"barn",
		"couches",
		"dock",
		"dreamer",
		"dress",
		"earth",
		"germ",
		"island",
		"paragraph",
		"shark",
		"shrimp",
		"swamp",
		"table",
		"tool",
		"whale"
	]

    # generate random numbers whole numbers from python
	from random import randint

	# create variables
	spelling_word = spelling_list[randint(0,14)]

	# IF REQUEST METHOD IS A POST 
	if request.method == "POST":
		# GRAB IN THE FORM AND STICK IN VARIABLE
		answer = request.POST['answer']
		# pass num1 and num2 from frontend
		spelling_img = request.POST['spelling_img']
		# error handling if the answer is empty
		if not answer:
			my_answer = "Please try again! "
			color = 'warning'
			return render(request, 'reading.html', {
			'answer':answer,
			'my_answer':my_answer,
			'spelling_word': spelling_word,
			'color': color,
			}) 

		# comparision code / determine correct answer 
		if str(answer) == spelling_word:
			my_answer = "Correct!  " + answer + " is the correct spelling."
			color = "success " # color of the pop up box from boostrap
		else:
			my_answer = "Incorrect! The correct spelling is: " + str(spelling_word)
			color = "danger " # color of the pop up box from boostrap

		# CONTEXT DICTIONARY returns to the screen 
		return render(request, 'reading.html', {
			'answer':answer,
			'my_answer':my_answer,
			'spelling_word': spelling_word,
			'color': color, # pass in color for pop up box 
			}) 
	# initial start 
	return render(request,'reading.html', {
			'spelling_word': spelling_word,
			})

# Create your views here.
def about(request):
    return render(request, 'about.html', {})

# Create your views here.
def contact(request):
	return render(request, 'contact.html', {})



  

# Create your views here.
def confirmation(request):
	return render(request, 'confirmation.html', {})
  

# Create your views here.
def subscribe(request):
	return render(request, 'subscribe.html', {})
