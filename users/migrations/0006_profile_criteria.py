# Generated by Django 3.0.8 on 2020-08-06 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0014_auto_20200806_0238'),
        ('users', '0005_auto_20200805_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='criteria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='fixpol.Criteria'),
        ),
    ]
