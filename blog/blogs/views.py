from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blogs.models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
def homeview(request):
    context={"post":Post.objects.all()}
    return render(request,"blogs/home.html",context)
def aboutview(request):
    return render(request,"blogs/about.html",{"title":"about"})
class postlistview(ListView):
    model=Post
    template_name="blogs/home.html"
    context_object_name='post'
    ordering=["-date_posted"]
    paginate_by=2
class postdetailview(DetailView):
    model=Post
class postcreateview(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title',"content"]
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class postupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=["title","content"]
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
class postdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False
class userpostlistview(ListView):
    model=Post
    template_name="blogs/userpost.html"
    context_object_name="post"
    paginate_by=2
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")
# Create your views here.
