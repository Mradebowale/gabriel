from django.shortcuts import render, redirect
from .models import Job, Applicant
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("Gender")
        email = request.POST.get("email")
        home_address = request.POST.get("home_address")
        phone_number = request.POST.get("phone_number")
        job_interest = request.POST.get("job_aspired")
        valid_id = request.POST.get("valid_id")
        image = request.FILES.get("image")
        previous_place = request.POST.get("previous_workplace")

        Applicant.objects.create(First_name=first_name, Middle_name=middle_name, 
                                 Last_name=last_name, Gender=gender, 
                                 email=email, Home_address=home_address, Phone_number=phone_number,
                                 Job_aspired=job_interest, Id_document=valid_id, Id_image=image,
                                 Former_workplace=previous_place)
        messages.success(request, "Application Info submitted")

    return render(request, "job/index.html")

@login_required
def jobuploads(request):
    if request.method == "POST":
        form = jobform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Job uploaded successfully")
    else:
        form = jobform()
    return render(request, 'job/new-post.html', {'form': form})




from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

def logins(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('job')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



# from django.shortcuts import render, redirect
# from .forms import UserRegistrationForm

# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'register_template.html', {'form': form})


def applynow(request):
    return render(request, "job/appform.html")