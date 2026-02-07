from django.shortcuts import render, redirect
from django.http import HttpResponse
from Data.models import *
def contactform(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        en=contact(name=name,email=email,subject=subject,message=message)
        en.save()
    return render(request,"success.html")

def home(request):
    home_datadata = home_data.objects.all()[:1]
    aboutdata = about.objects.all()[:2]
    social_linkdata = social_link.objects.all()
    emaildata = email.objects.all()[:1]
    phonedata = phone.objects.all()[:1]
    locationdata = location.objects.all()[:1]
    projectdata = project.objects.all()
    experiencesdata = Experiences.objects.all()
    Educationdata = Education.objects.all()
    birthdaydata = birthday.objects.all()[:1]
    certificationsdata = certifications.objects.all()
    Achievementsdata = Achievements.objects.all()
    Training_coursesdata = Training_courses.objects.all()
    Articlesdata = Articles.objects.all()
    mediumdata = medium.objects.all()[:1]
    profileimgdata = profileimg.objects.all()[:1]
    workdata = work.objects.all()
    testimonialdata =testimonial.objects.all
    clientdata = client.objects.all()
    DEFskillsdata = skills.objects.filter(skill_category='Defensive')
    ATKskillsdata = skills.objects.filter(skill_category='Attacking')
    PROskillsdata = skills.objects.filter(skill_category='Programming')
    DSCskillsdata = skills.objects.filter(skill_category='Data_science')
    AIskillsdata = skills.objects.filter(skill_category='Artificial_Intelligence')
    TATskillsdata = skills.objects.filter(skill_category='Tools_and_Technologies')
    OTSskillsdata = skills.objects.filter(skill_category='Others')
    skilldata = topskill.objects.all()
    loc_data = home_loc.objects.all()[:1]

        
    data = {
        'DEFskillsdata':DEFskillsdata,
        'ATKskillsdata':ATKskillsdata,
        'PROskillsdata':PROskillsdata,
        'DSCskillsdata':DSCskillsdata,
        'AIskillsdata':AIskillsdata,
        'TATskillsdata':TATskillsdata,
        'OTSskillsdata':OTSskillsdata,
        'home_datadata':home_datadata,
        'aboutdata':aboutdata,
        'social_linkdata':social_linkdata,
        'emaildata':emaildata,
        'phonedata':phonedata,
        'locationdata':locationdata,
        'projectdata':projectdata,
        'experiencesdata':experiencesdata,
        'Educationdata':Educationdata,
        'certificationsdata':certificationsdata,
        'Achievementsdata':Achievementsdata,
        'Training_coursesdata':Training_coursesdata,
        'Articlesdata':Articlesdata,
        'mediumdata':mediumdata,
        'profileimgdata':profileimgdata,
        'birthdaydata':birthdaydata,
        'workdata':workdata,
        'testimonialdata':testimonialdata,
        'clientdata':clientdata,
        'skilldata':skilldata,
        'loc_data':loc_data,
    }
    return render(request,"index.html",data)