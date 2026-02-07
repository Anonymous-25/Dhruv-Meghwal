from django.db import models

# Create your models here.
class home_data(models.Model):
    home_icon = models.CharField(max_length=5000)
    name = models.CharField(max_length=150)
    home_profession = models.CharField(max_length=5000)
    home_Description = models.TextField()

class about(models.Model):
    about_Description = models.TextField()

class social_link(models.Model):
    social_url = models.CharField(max_length=5000)
    social_name = models.CharField(max_length=150)
    social_icon = models.CharField(max_length=5000)

class email(models.Model):
    email_icon = models.CharField(max_length=150)
    email_name = models.CharField(max_length=150)
    email_address = models.CharField(max_length=250)

class phone(models.Model):
    phone_number = models.CharField(max_length=13)

class location(models.Model):
    location_name = models.CharField(max_length=150)


    


class skills(models.Model):
    category = [
        ('Defensive','Defensive'),
        ('Attacking','Attacking'),
        ('Programming','Programming'),
        ('Data_science','Data science'),
        ('Artificial_Intelligence','Artificial Intelligence'),
        ('Tools_and_Technologies','Tools & Technologies'),
        ('Others','Others')
        
    ]
    skill_title = models.CharField(max_length=150)
    skill_icon = models.CharField(max_length=5000)
    skill_category = models.CharField(max_length=200,choices=category,default='Defensive')
    


class language(models.Model):
    name1 = models.CharField(max_length=100)
    def __str__ (self):
        return self.name1

class project(models.Model):

    project_name =models.CharField(max_length=150)
    project_github = models.CharField(max_length=2000)
    project_img = models.CharField(max_length=2000)
    project_description = models.TextField()
    project_language = models.ForeignKey(language,on_delete=models.CASCADE)    

class Experiences(models.Model):
    location1 = [
        ('Company','Company'),
        ('Website','Website'),
        ('Institution','Institution'),
        ('School','School'),
        ('Competition','Competition'),
        ('CTF','CTF'),
        ('me','me')
        
    ]
    Ex_post = models.CharField(max_length=150)
    Ex_for = models.CharField(max_length=20,choices=location1,default='SC')
    Ex_forname = models.CharField(max_length=150)
    Ex_date = models.CharField(max_length=150)
    Ex_works = models.TextField(max_length=2000)

class Education(models.Model):
    Title = models.CharField(max_length=2000)
    Provider_location = models.CharField(max_length=2000)
    Time_duration = models.CharField(max_length=2000)
    score = models.CharField(max_length=150)


class certifications(models.Model):
    Provider_logo = models.CharField(max_length=2000)
    Provider_name = models.CharField(max_length=2000)
    Certifiate_name = models.CharField(max_length=2000)
    
class Achievements(models.Model):
    Ach_logo = models.CharField(max_length=2000)
    Ach_title = models.CharField(max_length=2000)
    Ach_description = models.TextField()

class Training_courses(models.Model):
    Tra_logo = models.CharField(max_length=2000)
    Tra_title = models.CharField(max_length=2000)
    Tra_description = models.TextField()

class Articles(models.Model):
    Art_Background = models.CharField(max_length=2000)
    Tra_title = models.CharField(max_length=2000)
    Tra_date = models.CharField(max_length=2000)
    Tra_description = models.TextField()
    Tra_link = models.CharField(max_length=2000)

class medium(models.Model):
    mediumacc = models.CharField(max_length=2000)

class profileimg(models.Model):
    profile_src = models.CharField(max_length=2000)

class birthday(models.Model):
    birthday_date = models.CharField(max_length=2000)

class work(models.Model):
    work_icon = models.CharField(max_length=2000)
    work_title = models.CharField(max_length=2000)
    work_description = models.CharField(max_length=2000)
    

class contact(models.Model):
    idd = models.CharField(max_length=1000)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
class testimonial(models.Model):
    name = models.CharField(max_length=150)
    message = models.CharField(max_length=2000)

class client(models.Model):
    name = models.CharField(max_length=150)

class topskill(models.Model):
    name = models.CharField(max_length=150)
    skill_percent = models.CharField(max_length=3)

class home_loc(models.Model):
    home_location = models.URLField(max_length=5000)