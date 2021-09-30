from django.shortcuts import render
from .models import MyInfo
from .models import Education
from .models import Experience
from .models import Interest
from .models import Skills
from .models import Awards
# Create your views here.
def info(request):
    info = MyInfo.objects.get()
    data = {'info':info}
    return render(request,"portfolio/myInfo.html",data)

def homepage(request):
    return render(request,"portfolio/landing.html")

def education(request):
    edu = Education.objects.all()
    data = {'edu':edu}
    return render(request,"portfolio/education.html",data)

def experience(request):
    exp =Experience.objects.all()
    data = {'exp':exp}
    return render(request,"portfolio/experience.html",data)
def interest(request):
    inte = Interest.objects.all()
    data = {'inte':inte}
    return render(request,"portfolio/interest.html",data)
def skills(request):
    skill = Skills.objects.all()
    data = {'skill':skill}
    return render(request,"portfolio/skills.html", data)
def awards(request):
    award = Awards.objects.all()
    data = {'award':award}
    return render(request,"portfolio/awards.html",data)
