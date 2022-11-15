from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    gender_options = (('male', 'Male'), ('female', 'Female'))
    date_of_birth = models.DateField()
    gender = models.CharField(choices=gender_options, max_length=6)
    phone = models.CharField(max_length=10)
    # group= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# class UserType(models.Model):
#     type = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.type
