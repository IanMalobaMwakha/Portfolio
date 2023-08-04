# Generated by Django 4.2.3 on 2023-08-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tools_name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Projects Section: Tools and Technologies Used',
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Projects Section: Project'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='tools_and_lang',
        ),
        migrations.AddField(
            model_name='project',
            name='tools_and_lang',
            field=models.ManyToManyField(blank=True, max_length=255, null=True, to='core.toolsused'),
        ),
    ]
