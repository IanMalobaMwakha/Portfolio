# Generated by Django 4.2.7 on 2023-11-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_project_project_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'PROJECTS SECTION'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='tools_and_lang',
        ),
        migrations.AlterField(
            model_name='project',
            name='live_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='ToolsUsed',
        ),
    ]
