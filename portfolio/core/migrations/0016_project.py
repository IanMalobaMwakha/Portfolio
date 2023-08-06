# Generated by Django 4.2.3 on 2023-08-04 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_education_options_alter_experience_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('github_link', models.CharField(blank=True, max_length=255, null=True)),
                ('live_link', models.CharField(max_length=255, null=True)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='project_images')),
                ('project_short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('project_description', models.TextField(blank=True, null=True)),
                ('tools_and_lang', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ['-created_at'],
            },
        ),
    ]