# Generated by Django 3.2.16 on 2022-11-14 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0004_remove_parent_user_type'),
        ('student', '0003_remove_student_user_type'),
        ('userextend', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
