# Generated by Django 3.2.7 on 2021-10-05 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parent_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_departments', to='core.department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='core.department')),
            ],
        ),
    ]