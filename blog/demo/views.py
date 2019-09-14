from django.shortcuts import render
from demo.forms import feedbackform
def feedbackview(request):
    form=feedbackform()
    if request.method=="POST":
        form=feedbackform(request.POST)
        if form.is_valid():
            print("form validation succes")
    return render(request,"demo/feedback.html",{"form":form})

# Create your views here.
