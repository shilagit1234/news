# Generated by Django 3.1.7 on 2021-05-10 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('i', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_mobile',
            new_name='student_full_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='student_mobile_no',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_reg_number',
            new_name='student_roll_number',
        ),
    ]
