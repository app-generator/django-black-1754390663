# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Demo(models.Model):

    #__Demo_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Demo_FIELDS__END

    class Meta:
        verbose_name        = _("Demo")
        verbose_name_plural = _("Demo")


class Demo3(models.Model):

    #__Demo3_FIELDS__
    number = models.BooleanField()

    #__Demo3_FIELDS__END

    class Meta:
        verbose_name        = _("Demo3")
        verbose_name_plural = _("Demo3")



#__MODELS__END
