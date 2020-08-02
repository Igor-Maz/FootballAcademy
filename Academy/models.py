import datetime
from django.db import models
from Accounts.models import Profile
from Academy.validators import number_on_tshirt

TYPE = (
    (1, "Chłopcy"),
    (2, "Dziewczynki"),
    (3, "Wspólny")
)


# admin
class TeamType(models.Model):
    age_class = models.IntegerField(verbose_name='Grupa wiekowa')
    sex = models.IntegerField(verbose_name='Płeć', choices=TYPE)

    def __str__(self):
        return f"U{self.age_class} - {self.get_sex_display()}"


class Player(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name='Profil')
    sex = models.IntegerField(verbose_name='Płeć', choices=(
        (1, "Chłopiec"),
        (2, "Dziewczynka")
    ), null=True, blank=True)
    position = models.IntegerField(verbose_name='Pozycja na boisku', choices=(
        (1, "Bez pozycji"),
        (2, "Bramkarz"),
        (3, "Obrońca"),
        (4, "Pomocnik"),
        (5, "Napastnik")
    ), null=True, blank=True)
    favourite_number = models.IntegerField(verbose_name='Preferowany numer na koszulce',
                                           validators=[number_on_tshirt], null=True, blank=True)

    def __str__(self):
        return self.profile.username

    def get_detail_url(self):
        return f'/player/{self.id}'

    def get_age(self):
        age = datetime.date.today().year - self.profile.year_of_birth
        return age


class Team(models.Model):
    name = models.CharField(verbose_name='Nazwa', max_length=32)
    type = models.ForeignKey(TeamType, on_delete=models.CASCADE, verbose_name='Kategoria zespołu')
    description = models.TextField(verbose_name='Parę słów o zespole', null=True, blank=True)
    coach = models.ManyToManyField(Profile, related_name='Coach', verbose_name='Trener')
    staff = models.ManyToManyField(Profile, related_name='Staff', verbose_name='Pracownicy w zespole')
    players = models.ManyToManyField(Player,
                                     verbose_name='Zawodnicy w zespole')  # zastanowic sie nad many to one relation w modelu gracz

    def __str__(self):
        return f"{self.name}"

    def get_detail_url(self):
        return f'/team/{self.id}'


class Fan(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name='Profil')
    favourite_players = models.ManyToManyField(Player, verbose_name='Ulubieni gracze', null=True, blank=True)
    favourite_teams = models.ManyToManyField(Team, verbose_name='Ulubione zespoły', null=True, blank=True)

    def __str__(self):
        return f"{self.profile.username}"
