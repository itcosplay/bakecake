# Generated by Django 4.0.4 on 2022-04-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('n', 'Новый'), ('unpay', 'Неоплачен'), ('pay', 'Оплачен'), ('a', 'Принят'), ('p', 'Готовится'), ('d', 'Передан в доставку'), ('c', 'Выполнен')], default='n', max_length=20, verbose_name='Статус заказа'),
        ),
    ]
