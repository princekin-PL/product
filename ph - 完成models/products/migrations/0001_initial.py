# Generated by Django 3.0.7 on 2020-06-26 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='例：抖音-用短视频记录生活', max_length=50)),
                ('intro', models.TextField(default='这里写APP简介')),
                ('url', models.CharField(default='Http://', max_length=100)),
                ('icon', models.ImageField(default='default_icon.png', upload_to='images/')),
                ('image', models.ImageField(default='default_image.jpg', upload_to='images/')),
                ('votes', models.IntegerField(default=1)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
