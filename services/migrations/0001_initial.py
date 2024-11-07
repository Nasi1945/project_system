# Generated by Django 4.2 on 2024-11-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('content', models.TextField(default='کمک کننده')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('content', models.TextField(default='این سرویس کار شما را راحت تر کرده است')),
                ('image', models.ImageField(default='service.jpg', upload_to='services')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('attribute', models.ManyToManyField(to='services.attribute')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]