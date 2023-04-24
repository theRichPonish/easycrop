# Generated by Django 3.2.3 on 2021-08-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop_prediction_ai', '0010_rename_pontact_number_advertisement_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='contact_Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='payment_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='payment_method',
            field=models.CharField(max_length=5000),
        ),
    ]
