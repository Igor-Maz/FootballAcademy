from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(verbose_name='Ksywka', max_length=30, null=True, blank=True)
    first_name = models.CharField(verbose_name='Imię', max_length=30, null=True, blank=True)
    last_name = models.CharField(verbose_name='Nazwisko', max_length=150, null=True, blank=True)
    description = models.TextField(verbose_name='Parę słów o sobie', null=True, blank=True)
    year_of_birth = models.IntegerField(verbose_name='Data urodzenia', null=True, blank=True)
    in_academy_since = models.IntegerField(verbose_name='W akademi od', null=True, blank=True)
    role = models.IntegerField(verbose_name='Rola', default=4, choices=(
        (1, "Coach"),
        (2, "Staff"),
        (3, 'Player'),
        (4, 'Fan')
    ))
    salary = models.IntegerField(verbose_name='Wynagrodzenie za godzinę', null=True, blank=True)

    def __str__(self):
        return self.username

    def get_detail_url(self):
        return f'/profile/{self.id}'
