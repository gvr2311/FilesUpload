from django.shortcuts import render
from .forms import *
from .models import *

def Index(request):
    return render(request, "profiles/index.html")

# Create your views here.
def Profiles(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            #n1 = form.cleaned_data.get("fname")
            form.save()
            obj = form.instance
            return render(request,"profiles/profile.html",{'form':form, "obj":obj})            
        else:
            return render(request, "profiles/profile.html", {'form':form})
    else:
        form = ProfileForm()        
        return render(request, "profiles/profile.html", {'form':form})

def GetProfiles(request):
    if request.method == 'GET':
        rows = Info.objects.all()
        return render(request, 'profiles/getprofiles.html', {'rows': rows})

