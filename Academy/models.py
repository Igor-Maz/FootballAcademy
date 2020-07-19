from django.db import models
from Academy.validators import number_on_tshirt, test_result

TYPE = (
    (1, "Boys"),
    (2, "Girls"),
    (3, "Coeducational")
)

# admin
class TeamType(models.Model):
    age_class = models.IntegerField(verbose_name='Grupa wiekowa')
    sex = models.IntegerField(verbose_name='Płeć', choices=TYPE)

    def __str__(self):
        return f"U{self.age_class} - {self.sex}"


class Coach(models.Model):
    # user = models.OneToOneField(User)
    first_name = models.CharField(verbose_name='Imię', max_length=20)
    last_name = models.CharField(verbose_name='Nazwisko', max_length=20)
    description = models.TextField(verbose_name='Parę słów o sobie', null=True, blank=True)
    year_of_birth = models.IntegerField(verbose_name='Data urodzenia', null=True, blank=True)
    certificated = models.BooleanField(verbose_name='Certyfikat')
    in_academy_since = models.IntegerField(verbose_name='W akademi od')
    salary = models.IntegerField(verbose_name='Wynagrodzenie za godzinę')

    def __str__(self):
        return f"Trener - {self.first_name} {self.last_name}"

    def get_detail_url(self):
        return f'/coach/{self.id}'


class Stuff(models.Model):
    first_name = models.CharField(verbose_name='Imię', max_length=20)
    last_name = models.CharField(verbose_name='Nazwisko', max_length=20)
    role = models.CharField(verbose_name='Rola', max_length=64)
    description = models.TextField(verbose_name='Parę słów o sobie', null=True, blank=True)
    salary = models.IntegerField(verbose_name='Wynagrodzenie za godzinę')

    def __str__(self):
        return f"{self.role} - {self.first_name} {self.last_name}"

    def get_detail_url(self):
        return f'/stuff/{self.id}'


class Player(models.Model):
    first_name = models.CharField(verbose_name='Imię', max_length=20)
    last_name = models.CharField(verbose_name='Nazwisko', max_length=20)
    nickname = models.CharField(verbose_name='Ksywka na koszulce', max_length=10)
    description = models.TextField(verbose_name='Parę słów o sobie', null=True, blank=True)
    year_of_birth = models.IntegerField(verbose_name='Data urodzenia', validators=[])
    sex = models.IntegerField(verbose_name='Płeć', choices=(
                                    (1, "Boy"),
                                    (2, "Girl")
                                ))
    in_academy_since = models.IntegerField(verbose_name='W akademi od')
    role = models.IntegerField(verbose_name='Pozycja na boisku', choices=(
                                    (1, "Unclassified"),
                                    (2, "Goalkeeper"),
                                    (3, "Defender"),
                                    (4, "Midfielder"),
                                    (5, "Forward")
                                ))
    favourite_number = models.IntegerField(verbose_name='Preferowany numer na koszulce',
                                           validators=[number_on_tshirt])

    def __str__(self):
        return f"{self.nickname}"

    def get_detail_url(self):
        return f'/player/{self.id}'


class Team(models.Model):
    name = models.CharField(verbose_name='Nazwa', max_length=32)
    description = models.TextField(verbose_name='Parę słów o zespole', null=True, blank=True)
    coach = models.ManyToManyField(Coach, through='TeamCoaches', verbose_name='Trener', null=True, blank=True)
    type = models.ForeignKey(TeamType, on_delete=models.CASCADE, verbose_name='Kategoria zespołu')
    stuff = models.ManyToManyField(Stuff, verbose_name='Pracownicy w zespole')
    players = models.ManyToManyField(Player, verbose_name='Zawodnicy w zespole') #zastanowic sie nad many to one relation w modelu gracz

    def __str__(self):
        return f"{self.name}"

    def get_detail_url(self):
        return f'/team/{self.id}'

# admin
class TeamCoaches(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Zespół')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name='Trener')
    role = models.IntegerField(verbose_name='Rola trenera', choices=(
                                    (1, "Primary"),
                                    (2, "Secondary")
                                ))


class Supporter(models.Model):
    name = models.CharField(verbose_name='Imię', max_length=64)
    description = models.TextField(verbose_name='Parę słów o sobie', null=True, blank=True)
    supporting_players = models.ManyToManyField(Player, verbose_name='Obserwuję graczy')
    supporting_teams = models.ManyToManyField(Team, verbose_name='Obserwuję zespoły')

    def __str__(self):
        return f"{self.name}"

# admin
class DayName(models.Model):
    name = models.CharField(max_length=16)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.name}'


class Test(models.Model):
    name = models.CharField(verbose_name='Nazwa', max_length=64)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name='Trener')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Zespół')
    players = models.ManyToManyField(Player, through='TestResults', verbose_name='Zawodnik')
    date = models.DateTimeField(verbose_name='Data testu')
    week_day = models.ForeignKey(DayName, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_detail_url(self):
        return f'/test/{self.id}'


class TestResults(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Test')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Zawodnik')
    result = models.FloatField(validators=[test_result], verbose_name='Wynik testu')
    description = models.TextField(null=True, blank=True, verbose_name='Opis')


class Match(models.Model):
    our_team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Nasz zespół')
    our_team_score = models.IntegerField(verbose_name='Nasz wynik')
    enemy_team = models.CharField(max_length=32, verbose_name='Przeciwnik')
    enemy_team_score = models.IntegerField(verbose_name='Wynik przeciwnika')
    home = models.BooleanField(verbose_name='Gramy u siebie')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name='Trener')
    date = models.DateTimeField(verbose_name='Data meczu')
    week_day = models.ForeignKey(DayName, on_delete=models.CASCADE)
    match_type = models.IntegerField(verbose_name='Rodzaj spotkania', choices=(
                                    (1, "Official"),
                                    (2, "Sparing")
                                ))
    squad = models.ManyToManyField(Player, through='MatchSummary', verbose_name='Skład')
    description = models.TextField(verbose_name='Opis', null=True, blank=True)

    def __str__(self):
        if self.home == 1:
            return f"{self.our_team} - {self.enemy_team}"
        else:
            return f"{self.enemy_team} - {self.our_team}"

    def get_detail_url(self):
        return f'/match/{self.id}'


class MatchSummary(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name='Mecz')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Zawodnik')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name='Trener')
    goals = models.IntegerField(null=True, blank=True, verbose_name='Liczba bramek')
    cards = models.IntegerField(null=True, blank=True, verbose_name='Liczba kartek', choices=(
                                    (1, "Żółta"),
                                    (2, 'Czerwona')
                                ))
    rating = models.FloatField(validators=[test_result])


class Trainings(models.Model):
    name = models.CharField(verbose_name='Nazwa', max_length=32)
    description = models.TextField(verbose_name='Opis', null=True, blank=True)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name='Trener')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Zespół')
    # date = models.DateTimeField()
    week_day = models.ForeignKey(DayName, on_delete=models.CASCADE)
