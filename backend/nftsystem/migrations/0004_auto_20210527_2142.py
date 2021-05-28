# Generated by Django 3.2.3 on 2021-05-27 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nftsystem', '0003_alter_metadata_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='id',
        ),
        migrations.AlterField(
            model_name='metadata',
            name='token',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='nftsystem.basetoken'),
        ),
    ]
