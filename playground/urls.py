from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path("hello/", views.say_hello, name="hello"),
    path("members/", views.member_list, name="allmemebers"),
    path("addmembers/", views.add_member, name="addmember")
]