# Generated by Django 4.1.4 on 2023-01-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmotionBoard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_img',
            field=models.ImageField(blank=True, null=True, upload_to='diary/images/%Y/%m/%d/'),
        ),
    ]