# Generated by Django 4.2.3 on 2023-07-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='banco',
            field=models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa econômica'), ('ST', 'Santander'), ('BR', 'Bradesco')], max_length=4),
        ),
    ]
