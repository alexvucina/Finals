# Generated by Django 3.2.16 on 2022-11-14 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
