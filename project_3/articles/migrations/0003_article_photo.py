# Generated by Django 3.0 on 2022-05-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default='herseys.jpg', upload_to='gallary'),
        ),
    ]
