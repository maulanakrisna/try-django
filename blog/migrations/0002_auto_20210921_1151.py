# Generated by Django 3.2.7 on 2021-09-21 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
