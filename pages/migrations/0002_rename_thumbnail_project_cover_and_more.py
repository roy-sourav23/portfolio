# Generated by Django 4.1.7 on 2023-03-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='thumbnail',
            new_name='cover',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='details',
        ),
        migrations.AddField(
            model_name='project',
            name='codeLink',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='project',
            name='demo',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]
