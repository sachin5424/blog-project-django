# Generated by Django 3.1.7 on 2021-03-02 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_auto_20210301_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_Images',
            field=models.ImageField(upload_to='blog-images/'),
        ),
        migrations.CreateModel(
            name='Verfiy_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_otp', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]