from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.contrib import messages

from .forms import MemberForm

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # return HttpResponse("Hello World!")
    # return render(request, "hello.html")
    return render(request, "hello.html", {"name": "Django"})

def member_list(request):
    all_members = Member.objects.all()
    return render(request, "Members.html", {"members": all_members})

@csrf_exempt
def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member added successfully!')
            return redirect("allmemebers")
        else:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            age = request.POST.get('age')
            email = request.POST.get('email')
            passwd = request.POST.get('passwd')
            messages.success(request, "Form is not valid")
            # return redirect("addmember")
            return render(request, "addmember.html", {'lname': lname, 'fname': fname, 'age': age, 'email': email, 'passwd': passwd})

    else:
        return render(request, "addmember.html")