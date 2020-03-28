from annoying.fields import AutoOneToOneField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from byro.common.models.choices import Choices


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
    nachname = models.CharField(
            verbose_name=_('Nachname'),
            max_length=255,
            null=False,
            blank=False,
    )
    vermerk = models.TextField(
            verbose_name=_('Vermerk'),
            null=False,
            blank=True,
    )
    beitragsklasse = models.IntegerField(
            choices=Beitragsklasse.choices,
            verbose_name=_("Beitragsklasse"),
    )
    
    guardian = models.CharField(
            verbose_name=_('Gesetzlicher Vertreter'),
            max_length=255,
            null=False,
            blank=True,
    )

    is_address_wrong = models.BooleanField(default=False, verbose_name=_('Addresse fehlerhaft'))

class Beitragsklasse:
    NORMAL = 0
    STUDENT = 1
    U18 = 2
    PASSIV = 3
    SOZIAL = 4
    FAMILIE = 5

    @classproperty
    def choices(cls):
        return (
            (cls.NORNAL, _("Normal")),
            (cls.STUDENT, _("Student/Schüler ab 18")),
            (cls.U18, _("Jugend unter 18")),
            (cls.PASSIV, _("Passiv")),
            (cls.SOZIAL, _("Sozial")),
            (cls.FAMILIE, _("Familie")
