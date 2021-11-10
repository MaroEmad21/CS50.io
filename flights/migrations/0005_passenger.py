# Generated by Django 3.2.8 on 2021-10-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_auto_20211017_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]