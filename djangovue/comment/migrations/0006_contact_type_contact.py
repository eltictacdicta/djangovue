# Generated by Django 4.1.3 on 2022-11-21 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_contact_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='type_contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='comment.typecontact'),
        ),
    ]
