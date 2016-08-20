#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from list.models import Programme,inst,Category
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

@login_required(login_url='/list/login/')
def index(request):
	prog_list = Programme.objects.all()
	template = loader.get_template('list/index.html')
    	context = RequestContext(request, {
        	'prog_list': prog_list,
    	})
    	return HttpResponse(template.render(context))
@login_required(login_url='/list/login/')
def detail(request, prog_id):
	try:	
		prog = Programme.objects.get(pk=prog_id)
    	
    	except Programme.DoesNotExist:
        	raise Http404
    	return render(request, 'list/detail.html', {'prog': prog})

from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
class LostForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Email id', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    password1 = forms.CharField(label='Verify your password', max_length=100, widget=forms.PasswordInput)
class SignupForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.CharField(label='Your email id', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

from django.contrib.auth import authenticate, login
def login11(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
	return my_view(request)      
    else:
        form = NameForm()
	return render(request, 'list/name.html', {'form': form})

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
	    return index(request)
	else:
            return render(request, 'list/deactivate.html')
    else:
	return render(request, 'list/wrong.html')
	


def homepage(request):
	template = loader.get_template('list/homepage.html')
    	context = RequestContext(request)
    	return HttpResponse(template.render(context))

from django.contrib.auth.models import User
def signup(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        	form = SignupForm(request.POST)
		firstname = request.POST['first_name']
		lastname = request.POST['last_name']
		email = request.POST['email']
 	   	password = request.POST['password']
        	if form.is_valid():
			user = User.objects.create_user(firstname,email,password)
			user.last_name = lastname
			user.save()		
            		return index(request)
	else:
        	form = SignupForm()

        return render(request, 'list/signup.html', {'form': form})

def lost(request):
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        	form = LostForm(request.POST)
		username = request.POST['username']
	        email = request.POST['email']
 	   	password = request.POST['password']
		try:
 		    user = User.objects.get(email=email)
		except User.DoesNotExist:
    			user = None
               # user = User.objects.get(email=email)
        # check whether it's valid:
        	if user is None:
                        return render(request, 'list/noemail.html')
            	# process the data in form.cleaned_data as required
            	# ...
                else:
			user.set_password(password)
			user.save()
			return index(request)

	    	# if a GET (or any other method) we'll create a blank form
	else:
        	form = LostForm()
		return render(request, 'list/lost.html', {'form': form})


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render(request, 'list/homepage.html')
    # Redirect to a success page.

inst1 = inst.objects.all()
insti = []
for i in inst1:
	inst.append(i.name)
prog= (('chem','chem'),)
inst= (('IITB','IITB'),('IITD','IITD'),('IITC','IITC'),('IITK','IITK'))
cat= ((0,'GE'),(1,'GEPD'))
code= ((0,'A4109'),(1,'A4110'))
import csv;

class VisualForm(forms.Form):
	inst = forms.MultipleChoiceField(choices=inst, widget=forms.CheckboxSelectMultiple())
	prog = forms.MultipleChoiceField(choices=code, widget=forms.CheckboxSelectMultiple())
	cat = forms.MultipleChoiceField(choices=cat, widget=forms.CheckboxSelectMultiple())

@login_required(login_url='/list/login/')
def visual(request):
	if request.method == 'POST':
        	# create a form instance and populate it with data from the request:
        	form = VisualForm(request.POST)
		inst = request.POST.get('inst')
		prog = request.POST.get('prog')
		cat1 = request.POST.get('cat')
		ret= [2,4,6,8]
		for i in prog:
			i=int(i)
			#return HttpResponse(i)
			for j in cat1:
				#return HttpResponse(j)
				j=int(j)
				temp = Programme.objects.get(code=code[i][1])
				if cat[j][1] == 'GE':
					ret.append(temp.gec)
				if cat[j][1] == 'GEPD':
					ret.append(temp.gecpd)
                template = loader.get_template('list/visualize.html')
    		context = RequestContext(request, {
        		'ret': ret,
    		})

    		return HttpResponse(template.render(context))

	    	
	else:
        	form = VisualForm()

	return render(request, 'list/visual.html', {'form': form})

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime

@login_required(login_url='/list/login/')
def users(request):
    # Query all non-expired sessions
    sessions = Session.objects.filter(expire_date__gte=datetime.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    users =  User.objects.filter(id__in=uid_list)
    return render(request, 'list/users.html', {'users': users})

	
	

# Create your views here.
