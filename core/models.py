from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.mail import send_mail
import datetime

#username = admin
#password = 123
# Create your models here.

GROUP = (
    ('vegetable','Vegetable'),
    ('grain','Grain'),
    ('protein','Protien'),
    ('dairy','Dairy'),
    ('unknown','Unknown'),
)



class Kid(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField()

class Image(models.Model):
    kid = models.ForeignKey(Kid, on_delete = models.CASCADE)
    image_url =  models.URLField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now_add=True)
    is_apporved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete = models.CASCADE)
    food_group = models.CharField(max_length=10, choices= GROUP,default='unknown') 

    def save(self, *args, **kwargs):
        self.updated_on = datetime.datetime.now()
        if self.food_group == 'unknown':
            body = 'body'
            res = send_mail("Unknown Item uploaded", body, 'testiship1@gmail.com', [self.kid.email])
        return super().save(*args, **kwargs)