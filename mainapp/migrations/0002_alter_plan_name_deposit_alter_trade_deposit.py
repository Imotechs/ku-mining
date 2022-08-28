# Generated by Django 4.0.1 on 2022-08-04 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('option', models.CharField(blank=True, max_length=15)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('date_approved', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('cancel', models.BooleanField(default=False)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='trade',
            name='deposit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.deposit'),
        ),
    ]
