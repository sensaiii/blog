from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from users.forms import userupdateform,profileupdateform

# Create your views here.
def register(request):

    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"account creates for {username} !")
            return redirect("login")

    else:
        form=UserRegisterForm()
    return render(request,"users/register.html",{"form":form})
@login_required
def profile(request):
    if request.method=="POST":
       u_form=userupdateform(request.POST,instance=request.user)
       p_form=profileupdateform(request.POST,request.FILES,instance=request.user.profile)
       if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request,f"profile updated successesfully")
           return redirect("profile")
    else:
       u_form=userupdateform(instance=request.user)
       p_form=profileupdateform(instance=request.user.profile)
    context={"u_form":u_form,"p_form":p_form}
    return render(request,"users/profile.html",context)
#message. DEBUG:
# message.info
#message.success
#message.warming
#message.error
