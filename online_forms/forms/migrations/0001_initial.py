# Generated by Django 5.1.1 on 2024-09-09 22:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type', models.CharField(choices=[('text', 'text'), ('number', 'number'), ('email', 'email'), ('url', 'url'), ('date', 'date'), ('time', 'time'), ('checkbox', 'checkbox'), ('file', 'file')], max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('required', models.BooleanField(default=False)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.form')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.form')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.JSONField()),
                ('form_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.formfield')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_fields', to='forms.response')),
            ],
        ),
    ]
