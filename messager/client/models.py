from django.db import models

# Create your models here.

CITY =[  
         ("aa", "Addis Ababa"),
         ("naz","Nazrēt"),
         ("god", "Gonder"),
         ("mek","Mekele"),
         ("aws","Āwasa"),
         ("dd","Dire Dawa"),
         ("bah","Bahir Dar"),
         ("har", "Harar"),
         ("jig", "Jijiga"),
         ("aso", "Āsosa"),
         ("gam", "Gambēla"),
         ("sem", "Semera")
      ]

GENDER = [
     ('m',"Male"),
     ('f',"Female")
]

class Detail(models.Model):
     pub_date = models.DateTimeField(auto_now_add=True ,null=True)
     class Meta:
         abstract = True

class Myclient(Detail):
     first_name = models.CharField(max_length=50)
     middle_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     email     = models.EmailField(unique=True)
     gender    = models.CharField(max_length=3,choices=GENDER,default='m')
     phone     = models.CharField(max_length=12, blank=True,null=True)
     phoneb    = models.CharField(max_length=12, blank=True,null=True)
     coutry    = models.CharField(choices=CITY, max_length=3)
     class Meta:
          ordering = ["first_name","middle_name" ,"last_name",'gender', "email", "coutry","pub_date"]

class Account(Detail):
     user = models.ForeignKey(Myclient,on_delete=models.CASCADE,unique=True)
     password  = models.CharField(max_length=150)
     class Meta:
          ordering = ["user","password","pub_date"]

