# Generated by Django 4.2 on 2024-11-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_rename_attributes_staff_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(default='sstaff.jpg', upload_to='staff'),
        ),
    ]
