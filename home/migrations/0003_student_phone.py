# Generated by Django 5.0.6 on 2024-06-03 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
