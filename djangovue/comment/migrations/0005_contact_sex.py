# Generated by Django 4.1.3 on 2022-11-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_rename_typecontac_typecontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sex',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No binario')], default='N', max_length=1),
        ),
    ]
