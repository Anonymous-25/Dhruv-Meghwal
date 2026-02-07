from django.contrib import admin
from Data.models import *
class homeadmin (admin.ModelAdmin):
    list_display = ("home_icon","name","home_profession","home_Description")
# Register your models here.
class aboutadmin (admin.ModelAdmin):
    list_display = ("about_Description",)
# Register your models here.
class social_linkadmin (admin.ModelAdmin):
    list_display = ("social_url","social_name","social_icon")
# Register your models here.
class skillsadmin (admin.ModelAdmin):
    list_display = ("skill_title","skill_icon","skill_category",)
    list_filter = ('skill_category',)
# Register your models here.
class emailadmin (admin.ModelAdmin):
    list_display = ("email_icon","email_name","email_address")

class phoneadmin (admin.ModelAdmin):
    list_display = ("phone_number",)

class locationadmin (admin.ModelAdmin):
    list_display = ("location_name",)

class experiencesadmin (admin.ModelAdmin):
    list_display = ("Ex_post","Ex_forname","Ex_for","Ex_date","Ex_works")



class Educationadmin (admin.ModelAdmin):
    list_display = ("Title","Provider_location","Time_duration","score")

class certificationsadmin (admin.ModelAdmin):
    list_display = ("Provider_logo","Provider_name","Certifiate_name")

class Achievementsadmin (admin.ModelAdmin):
    list_display = ("Ach_logo","Ach_title","Ach_description")

class Training_coursesadmin (admin.ModelAdmin):
    list_display = ("Tra_logo","Tra_title","Tra_description")

class Articlesadmin (admin.ModelAdmin):
    list_display = ("Art_Background","Tra_title","Tra_description","Tra_link","Tra_date")

class contactsadmin (admin.ModelAdmin):
    list_display = ("idd","name","email","subject","message")

class mediumadmin (admin.ModelAdmin):
    list_display = ("mediumacc",)
class profileimgadmin (admin.ModelAdmin):
    list_display = ("profile_src",)
class birthdayadmin (admin.ModelAdmin):
    list_display = ("birthday_date",)
class workadmin (admin.ModelAdmin):
    list_display = ("work_icon","work_title","work_description")
class testimonialadmin (admin.ModelAdmin):
    list_display = ("name","message")
class clientadmin (admin.ModelAdmin):
    list_display = ("name",)
class topskilladmin (admin.ModelAdmin):
    list_display = ("name","skill_percent")
class home_locationadmin (admin.ModelAdmin):
    list_display = ("home_location",)

@admin.register(language)
class languageadmin(admin.ModelAdmin):
    pass

@admin.register(project)
class projectadmin(admin.ModelAdmin):
    pass

admin.site.register(home_data,homeadmin)
admin.site.register(home_loc,home_locationadmin)
admin.site.register(about,aboutadmin)
admin.site.register(social_link,social_linkadmin)
admin.site.register(skills,skillsadmin)
admin.site.register(email,emailadmin)
admin.site.register(phone,phoneadmin)
admin.site.register(location,locationadmin)
admin.site.register(Experiences,experiencesadmin)
admin.site.register(Education,Educationadmin)
admin.site.register(certifications,certificationsadmin)
admin.site.register(Achievements,Achievementsadmin)
admin.site.register(Training_courses,Training_coursesadmin)
admin.site.register(Articles,Articlesadmin)
admin.site.register(medium,mediumadmin)
admin.site.register(contact,contactsadmin)
admin.site.register(profileimg,profileimgadmin)
admin.site.register(birthday,birthdayadmin)
admin.site.register(work,workadmin)
admin.site.register(testimonial,testimonialadmin)
admin.site.register(client,clientadmin)
admin.site.register(topskill,topskilladmin)


