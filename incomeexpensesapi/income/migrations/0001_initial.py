# Generated by Django 3.1.3 on 2020-11-24 13:55

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
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('TRAVEL', 'TRAVEL'), ('FOOD', 'FOOD'), ('RENT', 'RENT'), ('OTHERS', 'OTHERS')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
