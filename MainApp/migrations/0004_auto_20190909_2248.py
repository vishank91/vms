# Generated by Django 2.2.4 on 2019-09-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20190909_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslider',
            name='title',
            field=models.CharField(default=None, max_length=50),
        ),
    ]