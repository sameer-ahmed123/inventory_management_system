# Generated by Django 3.2.14 on 2022-07-10 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20220710_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['published']},
        ),
    ]
