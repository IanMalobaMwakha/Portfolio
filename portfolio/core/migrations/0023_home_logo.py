# Generated by Django 4.2.7 on 2023-12-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_project_options_remove_project_tools_and_lang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='home_images'),
        ),
    ]
