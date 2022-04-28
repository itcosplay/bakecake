# Generated by Django 4.0.4 on 2022-04-28 14:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscription', models.CharField(blank=True, max_length=200, verbose_name='Надпись на торте')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Торты',
            },
        ),
        migrations.CreateModel(
            name='CakeBerry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_berry', models.CharField(max_length=15, verbose_name='Ягоды')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Ягода',
                'verbose_name_plural': 'Ягоды',
            },
        ),
        migrations.CreateModel(
            name='CakeDecor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_decor', models.CharField(max_length=15, verbose_name='Декор')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Декор',
                'verbose_name_plural': 'Декор',
            },
        ),
        migrations.CreateModel(
            name='CakeLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_count', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество уровней')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Уровень торта',
                'verbose_name_plural': 'Уровни торта',
            },
        ),
        migrations.CreateModel(
            name='CakeShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape', models.CharField(max_length=50, verbose_name='Форма')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Форма торта',
                'verbose_name_plural': 'Формы торта',
            },
        ),
        migrations.CreateModel(
            name='CakeTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_topping', models.CharField(max_length=50, verbose_name='Топпинг')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Топпинг',
                'verbose_name_plural': 'Топпинги',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Email заказчика')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес заказчика')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Discounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_name', models.CharField(max_length=10, verbose_name='Купон')),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Размер скидки')),
            ],
            options={
                'verbose_name': 'Купон',
                'verbose_name_plural': 'Купоны',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время регистрации заказа')),
                ('called_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Время звонка клиенту')),
                ('delivered_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Время доставки заказа')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='cakes.cake', verbose_name='Заказанный торт')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='cakes.customer', verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-registered_at'],
            },
        ),
        migrations.AddField(
            model_name='cake',
            name='berry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='berries', to='cakes.cakeberry', verbose_name='Ягоды'),
        ),
        migrations.AddField(
            model_name='cake',
            name='decor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decors', to='cakes.cakedecor', verbose_name='Декор'),
        ),
        migrations.AddField(
            model_name='cake',
            name='level_count',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='cakes.cakelevel', verbose_name='Количество уровней торта'),
        ),
        migrations.AddField(
            model_name='cake',
            name='shape',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shapes', to='cakes.cakeshape', verbose_name='Форма торта'),
        ),
        migrations.AddField(
            model_name='cake',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='cakes.caketopping', verbose_name='Топпинг'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='номер телефона')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=150, verbose_name='имя')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': '_ПОЛЬЗОВАТЕЛИ',
            },
        ),
    ]
