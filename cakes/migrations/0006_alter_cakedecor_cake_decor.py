# Generated by Django 4.0.4 on 2022-04-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0005_remove_customer_name_customer_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakedecor',
            name='cake_decor',
            field=models.CharField(blank=True, choices=[(None, 'Выберите декор'), ('pistachios', 'Фисташки'), ('meringue', 'Безе'), ('hazelnuts', 'Фундук'), ('pekan', 'Пекан'), ('marshmallow', 'Маршмеллоу'), ('marzipan', 'Марципан')], max_length=15, verbose_name='Декор'),
        ),
    ]
