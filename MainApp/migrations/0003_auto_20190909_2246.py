# Generated by Django 2.2.4 on 2019-09-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_videogalary'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='images')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='VideoGalary',
        ),
        migrations.AddField(
            model_name='birthday',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
