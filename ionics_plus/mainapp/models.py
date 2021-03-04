from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class contact_us(models.Model):
    Full_name = models.CharField(max_length = 75)
    email = models.CharField(max_length=75,blank=False, null= True)
    whatsapp_number = models.IntegerField(blank=False, null= True)
    country = models.CharField(max_length = 75 ,blank=False, null= True)
    subject = models.TextField()



class user_service(models.Model):
    services_choice = (('Home Work','Home Work') , ('Project','Project') , ('Course','Course'), ('Assignment','Assignment'),('Lab','Lab'))
    title = models.CharField(max_length = 75)
    services = models.CharField(max_length = 75 , choices = services_choice,null = True, blank = False)
    subject = models.TextField(null = True, blank = False)
    email = models.CharField(max_length=75,null = True, blank = False)
    whatsapp_number = models.IntegerField(null = True, blank = False)
    country = models.CharField(max_length = 75,null = True, blank = False )
    delivery_date =models.TextField(null = True, blank = False)
    file1 = models.FileField(null = False, blank = True)
    file2 = models.FileField(null = False, blank = True)
    file3 = models.FileField(null = False, blank = True)
    author = models.ForeignKey(User,default = None,on_delete=models.CASCADE,null = True, blank = False)
    created = models.DateTimeField(auto_now_add=True)


    true_false = (('True','True') , ('False','False'))

    solving = models.CharField(max_length = 75 , choices = true_false,null = False, blank = True)
    rejected = models.CharField(max_length = 75 , choices = true_false,null = False, blank = True)
    accepted = models.CharField(max_length = 75 , choices = true_false,null = False, blank = True)
    in_progress = models.CharField(max_length = 75 , choices = true_false,default=True)
    finished = models.CharField(max_length = 75 , choices = true_false,null = False, blank = True)

    Price = models.CharField(max_length = 75 , null = False, blank = True)

    solution_file_1 = models.FileField(null = False, blank = True)
    solution_file_2 = models.FileField(null = False, blank = True)
    solution_file_3 = models.FileField(null = False, blank = True)

    payment_file = models.FileField(null = False, blank = True)

    payment_link_Knet = models.CharField(max_length = 300 ,null = False, blank = True)

    payment_link_visa = models.CharField(max_length = 300 ,null = False, blank = True)

    

    