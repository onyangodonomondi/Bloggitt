# Generated by Django 3.1.2 on 2020-12-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_merge_20201211_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
