# Generated by Django 3.0.6 on 2020-05-28 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['pub_date']},
        ),
    ]