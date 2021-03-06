# Generated by Django 3.0.8 on 2020-07-31 02:45

import Academy.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField(choices=[(1, 'Chłopiec'), (2, 'Dziewczynka')], verbose_name='Płeć')),
                ('position', models.IntegerField(choices=[(1, 'Bez pozycji'), (2, 'Bramkarz'), (3, 'Obrońca'), (4, 'Pomocnik'), (5, 'Napastnik')], verbose_name='Pozycja na boisku')),
                ('favourite_number', models.IntegerField(validators=[Academy.validators.number_on_tshirt], verbose_name='Preferowany numer na koszulce')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Profile', verbose_name='Profil')),
            ],
        ),
        migrations.CreateModel(
            name='TeamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_class', models.IntegerField(verbose_name='Grupa wiekowa')),
                ('sex', models.IntegerField(choices=[(1, 'Chłopcy'), (2, 'Dziewczynki'), (3, 'Wspólny')], verbose_name='Płeć')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Parę słów o zespole')),
                ('coach', models.ManyToManyField(related_name='Coach', to='Accounts.Profile', verbose_name='Trener')),
                ('players', models.ManyToManyField(to='Academy.Player', verbose_name='Zawodnicy w zespole')),
                ('staff', models.ManyToManyField(related_name='Staff', to='Accounts.Profile', verbose_name='Pracownicy w zespole')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.TeamType', verbose_name='Kategoria zespołu')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite_players', models.ManyToManyField(to='Academy.Player', verbose_name='Ulubieni gracze')),
                ('favourite_teams', models.ManyToManyField(to='Academy.Team', verbose_name='Ulubione zespoły')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Profile', verbose_name='Profil')),
            ],
        ),
    ]
