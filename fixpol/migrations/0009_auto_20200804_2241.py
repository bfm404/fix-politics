# Generated by Django 3.0.8 on 2020-08-04 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0008_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='fixpol.Location'),
        ),
    ]
