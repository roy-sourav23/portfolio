# Generated by Django 4.1.7 on 2023-03-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_message_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='fname',
            field=models.CharField(max_length=120, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='message',
            name='lname',
            field=models.CharField(max_length=120, verbose_name='Last Name'),
        ),
    ]