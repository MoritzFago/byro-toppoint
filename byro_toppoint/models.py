from annoying.fields import AutoOneToOneField
from django.db import models

class ToppointProfile(models.Model):
    member = AutoOneToOneField(
            to='members.Member',
            on_delete=models.CASCADE,
            related_name='profile_toppoint',
    )
    vorname = models.CharField(
            verbose_name=_('Vorname'),
            max_length=255,
            null=False,
            blank=False,
    )
