from django.db import models
from client.models import Account,Detail
# Create your models here.

class Message(Detail):
     send_to = models.ForeignKey(Account,on_delete=models.CASCADE ,related_name="resiver")
     send_from = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='sender')
     detail  = models.TextField(blank=True)
     class Meta:
         ordering = ["send_to","send_from","detail","pub_date"]

     def is_self(self):
         if self.send_to == self.send_from:
             return True
         else:
             return False