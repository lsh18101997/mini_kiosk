# Generated by Django 5.0.3 on 2024-04-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0002_alter_menu_options_menu_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='img',
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='MENU_IMAGE'),
        ),
    ]
