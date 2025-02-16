# Generated by Django 3.2.25 on 2025-02-16 21:38

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juro', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('directDebt', models.BooleanField(default=False)),
                ('mb_reference', models.CharField(max_length=20)),
                ('mb_entity', models.CharField(max_length=20)),
                ('IBAN', models.CharField(max_length=36)),
                ('description', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='PlannedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isFixedDate', models.BooleanField(default=True)),
                ('cycle', models.CharField(choices=[('S', 'Semanal'), ('BiS', 'BiSemanal'), ('M', 'mensal'), ('Tri', 'Trimestral'), ('SeM', 'Semestral'), ('A', 'Anual')], max_length=4)),
                ('isFixedValue', models.BooleanField(default=True)),
                ('expectValue', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDebt', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=25)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('dateExpect', models.IntegerField()),
                ('businessDay', models.CharField(choices=[('A', 'Any Day'), ('BW', 'Business Day before weekend'), ('WB', 'Business Day after weekend')], max_length=3)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDebt', models.BooleanField(default=True)),
                ('value', models.FloatField()),
                ('dateRegister', models.DateField()),
                ('dateEffect', models.DateField()),
                ('personal', models.BooleanField(default=False)),
                ('creditCard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.creditcard')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.plannedevent')),
                ('monthRef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.month')),
                ('paymentReference', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.paymentreference')),
            ],
        ),
        migrations.AddField(
            model_name='plannedevent',
            name='series',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.transactionserie'),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='series',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.transactionserie'),
        ),
        migrations.CreateModel(
            name='AccountEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('activeHouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.house')),
                ('monthRef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finances.month')),
            ],
        ),
    ]
