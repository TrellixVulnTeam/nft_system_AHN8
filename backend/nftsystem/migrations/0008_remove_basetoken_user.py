# Generated by Django 3.2.3 on 2021-05-27 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nftsystem', '0007_alter_basetoken_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basetoken',
            name='user',
        ),
    ]
