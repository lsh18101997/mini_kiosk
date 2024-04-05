# Generated by Django 5.0.3 on 2024-04-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('price',), 'verbose_name': 'menu', 'verbose_name_plural': 'menus'},
        ),
        migrations.AddField(
            model_name='menu',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='MENU_IMAGE'),
        ),
    ]
