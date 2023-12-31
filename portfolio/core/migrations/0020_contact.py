# Generated by Django 4.2.3 on 2023-08-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_project_project_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_email', models.CharField(blank=True, max_length=255, null=True)),
                ('my_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedln', models.CharField(blank=True, max_length=255, null=True)),
                ('github', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('codepen', models.CharField(blank=True, max_length=255, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'CONTACT SECTION: Contact',
            },
        ),
    ]
