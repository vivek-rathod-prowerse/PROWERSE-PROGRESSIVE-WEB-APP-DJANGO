# Generated by Django 3.2.12 on 2022-04-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20220411_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadProductBulk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='PRODUCTFILE/')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadProductBulks',
        ),
    ]
