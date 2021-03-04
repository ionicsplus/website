from django.shortcuts import render,redirect
from .models import contact_us,user_service
from .forms import RegisterForm,ContactUs,AddingRequest,editform,paymentform
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
# Create your views here.

def main_app(request):

	if request.method == "POST":
		form = ContactUs(request.POST , request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()

			all_details = contact_us.objects.values().order_by('-id')[0]
			to_list = []
			to_list.append(all_details['email'])
			send_mail('From Ionics Plus','Thanks ' + all_details['Full_name'] + ' for using Ionics Plus, Your query has been received and we will contact you soon.','ionicsplus@gmail.com',to_list, fail_silently=False)
			print(to_list)
			send_mail('Query ' + all_details['Full_name'] +" country " + all_details['country'] ,'Query is ' + all_details['subject'] + " whats app Number is  " + str(all_details['whatsapp_number']) + " email: " + all_details['email'],all_details['email'],['ionicsplus@gmail.com'], fail_silently=False)
			return redirect('querydonepage')
	else:
		form = ContactUs()
   
	loged_in_user = request.user

	context = {'name':"Home" ,'user_name':loged_in_user,'form':form}

	return render(request,'mainapp/index.html',context)



def user_signup_page(request):

	if request.method == "POST":

		form = RegisterForm(request.POST)
		print("True")

		if form.is_valid():
			user = form.save()
			send_mail('New Sign up!','New user is Signed Up.','ionicsplus@gmail.com',['ionicsplus@gmail.com'], fail_silently=False)
			login(request,user)
			return redirect('mainapp')
	else:
		form = RegisterForm()

	context = {'title':'IONICS+ For Engineering Services','form':form}

	return render(request,'mainapp/signup.html',context)



def log_in_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('userpage')

    else:
        form = AuthenticationForm()
    context = {'form':form}

    return render(request,'mainapp/login.html',context)

def log_out_page(request):
    logout(request)
    return redirect('/')



def query_done_page(request):
	context = {'title':'IONICS+ For Engineering Services'}
	return render(request,'mainapp/querydone.html',context)


@login_required(login_url = '/login/')
def user_page(request):

	objs = user_service.objects.filter(author = request.user).order_by('-id')

	all_obj = user_service.objects.filter(author = request.user)

	loged_in_user = request.user

	try:
		latest_object = user_service.objects.filter(author = request.user).order_by('-id')[0]
	except:
		latest_object = ''

	context = {'title':'IONICS+ For Engineering Services','user_name':loged_in_user,'objs':objs ,'lastObject':latest_object, 'all_obj':all_obj}

	return render(request,'mainapp/userpage.html',context)



@login_required(login_url = '/login/')
def adding_request_page(request):

	if request.method == "POST":
		form = AddingRequest(request.POST , request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()

			all_details = user_service.objects.values().order_by('-id')[0]
			user_name = request.user.username

			print(user_name)
			to_list = []
			to_list.append(all_details['email'])
			send_mail('From Ionics Plus','Thanks ' + user_name + ' for using Ionics Plus, Your request has been received, please keep checking the request state on your website page.','ionicsplus@gmail.com',to_list, fail_silently=False)
			#print(to_list)
			send_mail('Request ' + user_name +" country " + all_details['country'] ,'Query type is ' + all_details['services'] + " .Subject is " + all_details['subject'] + " whats app Number is  " + str(all_details['whatsapp_number']) + " email: " + all_details['email'],all_details['email'],['ionicsplus@gmail.com'], fail_silently=False)
			return redirect('/requestsent/')
	else:
		form = AddingRequest()
	loged_in_user = request.user
	context = {'title':'IONICS+ For Engineering Services','user_name':loged_in_user,'form':form}
	return render(request,'mainapp/addrequestpage.html',context)


def request_sent_page (request):
	print()
	if not request.user.is_authenticated:
		return redirect('/')
	else:
		loged_in_user = request.user
		login(request,loged_in_user)
		context = {'title':'IONICS+ For Engineering Services','user_name':loged_in_user}
		return render(request,'mainapp/requestsent.html',context)


@user_passes_test(lambda u: u.is_superuser)
def control_page(request):
	objs = user_service.objects.all()
	loged_in_user = request.user
	context = {'user_name':loged_in_user, 'objs':objs}
	return render(request,'mainapp/control.html',context)


@user_passes_test(lambda u: u.is_superuser)
def edit_page(request,id):
	objs = user_service.objects.get(id=id)
	loged_in_user = request.user
	context = {'user_name':loged_in_user, 'objs':objs}
	return render(request,'mainapp/edit.html',context)


@user_passes_test(lambda u: u.is_superuser)
def update_page(request,id):
	objs = user_service.objects.get(id=id)

	#print(objs.title)

	if request.method == "POST":
		print(request.POST)
		form = editform(request.POST , request.FILES, instance=objs)
		print(form.errors)
		print("Done")

		if form.is_valid():
			print("wow1")
			form.save()
			print("wow2")
			messages.success(request,"Change updated successfully...")
		context = { 'objs':objs, 'form':form}
		return render(request,'mainapp/edit.html',context)




@login_required(login_url = '/login/')
def payment_page(request,id):
	objs = user_service.objects.get(id=id)
	loged_in_user = request.user

	print(objs.email)

	to_list = []
	to_list.append(objs.email)
	

	if request.method == "POST":
		form = paymentform(request.POST , request.FILES, instance=objs)
		
		if form.is_valid():
			form.save()
			messages.success(request,"Capture has been sent successfully...")
			send_mail('New Payment!','Payment from ID: ' + str(objs.id) + " title: " + objs.title,'ionicsplus@gmail.com',['ionicsplus@gmail.com'], fail_silently=False)
			send_mail('From Ionics Plus','Thanks ' + str(loged_in_user) + ' The payment capture has been received, please check the solution file on your website page.','ionicsplus@gmail.com',to_list, fail_silently=False)
	form = paymentform()
	context = {'title':'IONICS+ For Engineering Services','user_name':loged_in_user, 'objs':objs,'form':form,'messages':messages}
	return render(request,'mainapp/payment.html',context)
	

	
	
