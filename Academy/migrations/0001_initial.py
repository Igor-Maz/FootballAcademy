# Generated by Django 3.0.8 on 2020-07-15 19:40

import Academy.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=20, verbose_name='Nazwisko')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Parę słów o sobie')),
                ('year_of_birth', models.IntegerField(blank=True, null=True, verbose_name='Data urodzenia')),
                ('certificated', models.BooleanField(verbose_name='Certyfikat')),
                ('in_academy_since', models.IntegerField(verbose_name='W akademi od')),
                ('salary', models.IntegerField(verbose_name='Wynagrodzenie za godzinę')),
            ],
        ),
        migrations.CreateModel(
            name='DayName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('our_team_score', models.IntegerField(verbose_name='Nasz wynik')),
                ('enemy_team', models.CharField(max_length=32, verbose_name='Przeciwnik')),
                ('enemy_team_score', models.IntegerField(verbose_name='Wynik przeciwnika')),
                ('home', models.BooleanField(verbose_name='Gramy u siebie')),
                ('date', models.DateTimeField(verbose_name='Data meczu')),
                ('match_type', models.IntegerField(choices=[(1, 'Official'), (2, 'Sparing')], verbose_name='Rodzaj spotkania')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Coach', verbose_name='Trener')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=20, verbose_name='Nazwisko')),
                ('nickname', models.CharField(max_length=10, verbose_name='Ksywka na koszulce')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Parę słów o sobie')),
                ('year_of_birth', models.IntegerField(verbose_name='Data urodzenia')),
                ('sex', models.IntegerField(choices=[(1, 'Boy'), (2, 'Girl')], verbose_name='Płeć')),
                ('in_academy_since', models.IntegerField(verbose_name='W akademi od')),
                ('role', models.IntegerField(choices=[(1, 'Unclassified'), (2, 'Goalkeeper'), (3, 'Defender'), (4, 'Midfielder'), (5, 'Forward')], verbose_name='Pozycja na boisku')),
                ('favourite_number', models.IntegerField(validators=[Academy.validators.number_on_tshirt], verbose_name='Preferowany numer na koszulce')),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=20, verbose_name='Nazwisko')),
                ('role', models.CharField(max_length=64, verbose_name='Rola')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Parę słów o sobie')),
                ('salary', models.IntegerField(verbose_name='Wynagrodzenie za godzinę')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Parę słów o zespole')),
            ],
        ),
        migrations.CreateModel(
            name='TeamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_class', models.IntegerField(verbose_name='Grupa wiekowa')),
                ('sex', models.IntegerField(choices=[(1, 'Boys'), (2, 'Girls'), (3, 'Coeducational')], verbose_name='Płeć')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nazwa')),
                ('date', models.DateTimeField(verbose_name='Data testu')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Coach', verbose_name='Trener')),
            ],
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Nazwa')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Coach', verbose_name='Trener')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Team', verbose_name='Zespół')),
                ('week_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.DayName')),
            ],
        ),
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField(validators=[Academy.validators.test_result], verbose_name='Wynik testu')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Opis')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Player', verbose_name='Zawodnik')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Test', verbose_name='Test')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='players',
            field=models.ManyToManyField(through='Academy.TestResults', to='Academy.Player', verbose_name='Zawodnik'),
        ),
        migrations.AddField(
            model_name='test',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Team', verbose_name='Zespół'),
        ),
        migrations.AddField(
            model_name='test',
            name='week_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.DayName'),
        ),
        migrations.CreateModel(
            name='TeamCoaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(1, 'Primary'), (2, 'Secondary')], verbose_name='Rola trenera')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Coach', verbose_name='Trener')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Team', verbose_name='Zespół')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.ManyToManyField(through='Academy.TeamCoaches', to='Academy.Coach', verbose_name='Trener'),
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='Academy.Player', verbose_name='Zawodnicy w zespole'),
        ),
        migrations.AddField(
            model_name='team',
            name='stuff',
            field=models.ManyToManyField(to='Academy.Stuff', verbose_name='Pracownicy w zespole'),
        ),
        migrations.AddField(
            model_name='team',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.TeamType', verbose_name='Kategoria zespołu'),
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Imię')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Parę słów o sobie')),
                ('supporting_players', models.ManyToManyField(to='Academy.Player', verbose_name='Obserwuję graczy')),
                ('supporting_teams', models.ManyToManyField(to='Academy.Team', verbose_name='Obserwuję zespoły')),
            ],
        ),
        migrations.CreateModel(
            name='MatchSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField(blank=True, null=True, verbose_name='Liczba bramek')),
                ('cards', models.IntegerField(blank=True, choices=[(1, 'Żółta'), (2, 'Czerwona')], null=True, verbose_name='Liczba kartek')),
                ('rating', models.FloatField(validators=[Academy.validators.test_result])),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Coach', verbose_name='Trener')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Match', verbose_name='Mecz')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Player', verbose_name='Zawodnik')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='our_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.Team', verbose_name='Nasz zespół'),
        ),
        migrations.AddField(
            model_name='match',
            name='squad',
            field=models.ManyToManyField(through='Academy.MatchSummary', to='Academy.Player', verbose_name='Skład'),
        ),
        migrations.AddField(
            model_name='match',
            name='week_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academy.DayName'),
        ),
    ]
