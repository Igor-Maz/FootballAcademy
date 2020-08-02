from django.db import migrations
from Accounts.models import Profile

def populate(apps, schema_editor):
    Profile.objects.create(username='Pep', first_name='Pep', last_name='Guaro', description='Trener z pasją',
                           year_of_birth=1970, in_academy_since=2014, role=1, salary=200)
    Profile.objects.create(username='Hose', first_name='Jose', last_name='Mour', description='Jestem beznadziejny',
                           year_of_birth=1960, in_academy_since=2020, role=1, salary=20)
    Profile.objects.create(username='Franek', first_name='Franek', last_name='Smutna', description='Was?',
                           year_of_birth=1930, in_academy_since=2016, role=1, salary=60)
    Profile.objects.create(username='Heniu', first_name='Hansi', last_name='Flik', description='Trener na dorobku',
                           year_of_birth=1990, in_academy_since=2018, role=1, salary=100)
    Profile.objects.create(username='Jurgen', first_name='Jurek', last_name='Klos', description='Lubię heavy-metal',
                           year_of_birth=1984, in_academy_since=2013, role=1, salary=150)
    Profile.objects.create(username='Chrumka', first_name='Marta', last_name='Wac', description='Head Manager',
                           year_of_birth=1987, in_academy_since=2015, role=2, salary=150)
    Profile.objects.create(username='Bobi', first_name='Bogdan', last_name='Wim', description='Kierowca',
                           year_of_birth=1957, in_academy_since=2013, role=2, salary=50)
    Profile.objects.create(username='Robi', first_name='Robert', last_name='Kasprzyk', description='Kierowca',
                           year_of_birth=1967, in_academy_since=2018, role=2, salary=50)
    Profile.objects.create(username='Krysia', first_name='Krystyna', last_name='Mann', description='Kucharz',
                           year_of_birth=1964, in_academy_since=2016, role=2, salary=80)
    Profile.objects.create(username='Przemo', first_name='Przemek', last_name='Kuś', description='Masażysta',
                           year_of_birth=1989, in_academy_since=2019, role=2, salary=100)
    Profile.objects.create(username='Ann', first_name='Ania', last_name='Czar', description='Masażysta',
                           year_of_birth=1970, in_academy_since=2014, role=2, salary=120)
    Profile.objects.create(username='Ala', first_name='Alicja', last_name='Bog', description='Księgowa',
                           year_of_birth=1950, in_academy_since=2010, role=2, salary=150)
    Profile.objects.create(username='Lio', first_name='Lion', last_name='Mes', description='Szybki napastnik',
                           year_of_birth=2006, in_academy_since=2014, role=3)
    Profile.objects.create(username='Krysia', first_name='Krystyna', last_name='Ronalda', description='Będą mi stawiać pomniki',
                           year_of_birth=2001, in_academy_since=2016, role=3)
    Profile.objects.create(username='Prawy', first_name='Robert', last_name='Lewy', description='haha',
                           year_of_birth=2007, in_academy_since=2013, role=3)
    Profile.objects.create(username='Ansu', first_name='Anka', last_name='Fati', description='Dobrze sie zapowiada',
                           year_of_birth=2010, in_academy_since=2016, role=3)
    Profile.objects.create(username='Ney', first_name='Leya', last_name='Neya', description='Też dobrze sie zapowiada',
                           year_of_birth=2011, in_academy_since=2016, role=3)
    Profile.objects.create(username='Luki', first_name='Łukasz', last_name='Los', description='Gram w fifę',
                           year_of_birth=2007, in_academy_since=2014, role=3)
    Profile.objects.create(username='Kuba', first_name='Kuba', last_name='Ran', description='Czytam',
                           year_of_birth=2008, in_academy_since=2019, role=3)
    Profile.objects.create(username='Rafał', first_name='Rafał', last_name='Teraszak', description='Jeżdzę na rowerze',
                           year_of_birth=2006, in_academy_since=2012, role=3)
    Profile.objects.create(username='Dziki', first_name='Sam', last_name='Nowak', description='Będę dobry',
                           year_of_birth=2005, in_academy_since=2015, role=3)
    Profile.objects.create(username='Misiu', first_name='Michał', last_name='Nowak', description='Będę lepszy',
                           year_of_birth=2008, in_academy_since=2015, role=3)
    Profile.objects.create(username='Misia', first_name='Michalina', last_name='Nowak', description='A ja najlepsza',
                           year_of_birth=2010, in_academy_since=2015, role=3)


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
