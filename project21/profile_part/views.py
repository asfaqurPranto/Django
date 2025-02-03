from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
# from .forms import RegistrationForm
# Create your views here.
def base(request):
    return render(request,'base.html')

def login_page(request):
    return render(request,'login.html')

# def register_page(request):
#     return render(request,'register.html')


def register_page(request):
    if request.method == "POST":
        # form = RegistrationForm(request.POST)

            # Extract the form field values using get method
            username = request.POST.get('username')
            email = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            profile_username = request.POST.get('profile_username')
            city = request.POST.get('city')
            country = request.POST.get('country')
            bio = request.POST.get('bio')
            profession=request.POST.get('profession')

            # Check if a user with the same username already exists
            if User.objects.filter(username=username).exists():
                #form.add_error('username', 'Username already taken')
                messages.info(request, 'Username already taken')
                return redirect('/register/')

            # Create the user object
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            # Create the profile object
            profile = user.profile
            profile.phone = phone
            profile.profile_username = profile_username
            profile.city = city
            profile.country = country
            profession=profession
            profile.bio = bio

            profile.save()
            

            messages.success(request, 'Account created successfully')
            return redirect('/register/')
    

    
    return render(request, 'register.html')

def login_page(request):

    if request.method == "POST":       
        username = request.POST.get('username')
        email = username
        password = request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid user or password wrong')
            return redirect('/')
        else:
            login(request,user)
            return redirect('/home/')
    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('')

@login_required(login_url='/login/')
def home(request):
    queryset=Profile.objects.all()
    context={'prfls':queryset,'page':"HelpMe Homepage"}

    return render(request,'home.html',context)


@login_required(login_url='/login/')
def edit_profile(request):
    print("inside edit profile")
    return render(request,'edit_profile.html',{'page':request.user.profile.profile_username+"   |   Update"})

@login_required(login_url='/login/')
def view_profile(request):
    print("hi i am inside view my profile page")
    return render(request,'view_profile.html',{'page':request.user.profile.profile_username })



@login_required
def update_profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')  # Corrected 'username' to 'email'
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        profile_username = request.POST.get('profile_username')
        city = request.POST.get('city')
        country = request.POST.get('country')
        bio = request.POST.get('bio')
        profession = request.POST.get('profession')
        
        current_user=Profile.objects.get(id=request.user.id)
        print(country)
        current_user.country=country
        current_user.phone=phone
        current_user.city=city
        current_user.profession=profession
        current_user.bio=bio
        current_user.save()
        current_user.profile_username=profile_username
        current_user.save()
        
        current_user=User.objects.get(id=request.user.id)
        current_user.first_name=first_name
        current_user.last_name=last_name

        current_user.save()

    return redirect('/viewprofile/')



def subcatagory(request,name):
    if name=='it':
        jobs=['front end dev' ,'backend dev','data scientist','cyber security','Embeded system','IOT','ML','AI']
    elif name =='health':
        jobs=['Cardiologist' ,'Radiologist','Neurologist','Anesthesiologist','Psychiatrist','Surgeon','Gastroenterologist','Orthopaedist']
    return render(request,'subcatagory.html',context={'jobs':jobs})

# def show_that_profession(request,profession):

#     return render(request,'people_inside_profession.html',context={})

@login_required
def search_by_profession(request, profession):
    queryset = Profile.objects.filter(profession__icontains=profession)
    context = {'prfls': queryset}
    return render(request, 'search_result.html', context)


@login_required
def search_bar(request):
    if request.GET.get('search'):
         print('BCD')
    return render(request,'view_profile.html')

@login_required
def userdetails(request, email):
    queryset = Profile.objects.filter(user__email=email)
    context = {'queryset': queryset}
    return render(request, 'userdetails.html', context)

@login_required
def search_result(request):
    try:
        text = request.GET.get('search')
        #queryset = Profile.objects.filter(profile_username__icontains=text)

        #everything works fine here
        queryset1 = Profile.objects.filter(profile_username__icontains=text)
        queryset2 = Profile.objects.filter(profession__icontains=text)
        queryset3 = Profile.objects.filter(bio__icontains=text)
        queryset4 = Profile.objects.filter(city__icontains=text)

        # Use the union() method to combine the four querysets
        queryset = (
            queryset1
            .union(queryset2, all=False)
            .union(queryset3, all=False)
            .union(queryset4, all=False)
        )

       
        # Convert the queryset to a list of dictionaries
        queryset_data = list(queryset.values())
        
        # Store the list of dictionaries in the session
        request.session['search_result_queryset'] = queryset_data
        
    except ValueError:
        print("Error")
    
    context = {'text': text, 'queryset': queryset,'page':"Search result of "+ text}
    return render(request, 'search_result.html', context)

@login_required
def filterresult(request):
    try:
        search_by = request.GET.get('search_by')
        text = request.GET.get('query')
        
        # Retrieve the list of dictionaries from the session
        queryset_data = request.session.get('search_result_queryset')
        
        if queryset_data is None:
            # If data is not found in the session, create a new queryset
            queryset = Profile.objects.all()
            print("queryset is empty == problem")
        else:
            # Convert the list of dictionaries back to a QuerySet
            queryset = Profile.objects.filter(id__in=[item['id'] for item in queryset_data])

        if search_by == "city":
            queryset = queryset.filter(city__icontains=text)
        elif search_by == "name":
            queryset = queryset.filter(profile_username__icontains=text)
        else:
            queryset = queryset.filter(profession__icontains=text)
            
    except ValueError:
        print("Error")
    
    context = {'text': search_by, 'queryset': queryset}
    return render(request, 'search_result.html', context)

@login_required
def videocall(request):
    return render(request,'video_calling.html',{'name':request.user.username})