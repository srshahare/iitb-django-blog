# Generated by Django 3.2.4 on 2021-06-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_urltoimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='urlToImage',
            field=models.CharField(max_length=1000),
        ),
    ]
