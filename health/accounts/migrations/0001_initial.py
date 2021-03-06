# Generated by Django 2.2.15 on 2020-09-21 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=20, null=True)),
                ('religion', models.CharField(blank=True, choices=[('Agnostic', 'Agnostic'), ('Atheist', 'Atheist'), ('Buddhism', 'Buddhism'), ('Christianity', 'Christianity'), ('Hinduism', 'Hinduism'), ('Islam', 'Islam'), ('Judaism', 'Judaism'), ('Nonreligious', 'Non-religious'), ('Rastafarianism', 'Rastafarianism'), ('Other', 'Other')], max_length=20, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
