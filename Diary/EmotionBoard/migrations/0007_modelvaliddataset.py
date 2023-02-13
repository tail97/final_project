# Generated by Django 4.1.4 on 2023-01-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmotionBoard', '0006_alter_recommend_youtube_viewcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelValidDataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_return_emotion', models.CharField(default='', max_length=10, null=True)),
                ('user_select_emotion', models.CharField(default='', max_length=10, null=True)),
                ('comment', models.TextField()),
            ],
        ),
    ]