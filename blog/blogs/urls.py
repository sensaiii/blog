from django.urls import path
from blogs import views
from blogs.views import postlistview,postdetailview,postcreateview,postupdateview,postdeleteview,userpostlistview
app_name="blogs"
urlpatterns=[
#path("",views.homeview,name="blogs_home"),
path("",postlistview.as_view(),name="blogs_home"),
path("about/",views.aboutview,name="blogs_about"),
path("post/<int:pk>/",postdetailview.as_view(),name="post_detail"),
path("post/new/",postcreateview.as_view(),name="post_create"),
path("post/<int:pk>/update/",postupdateview.as_view(),name="post_update"),
path("post/<int:pk>/delete/",postdeleteview.as_view(),name="post_delete"),
path("user/<str:username>/",userpostlistview.as_view(),name="user_posts"),

]
