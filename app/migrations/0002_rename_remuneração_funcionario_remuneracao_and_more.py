# Generated by Django 5.1.4 on 2024-12-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='remuneração',
            new_name='remuneracao',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='data_nascimento',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11, unique=True),
        ),
    ]
