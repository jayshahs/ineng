# Generated by Django 4.0.5 on 2022-08-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='Username')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aux', models.CharField(default='Salt', max_length=16, verbose_name='aux')),
                ('quantity', models.IntegerField(default=1, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat', models.CharField(default='Beef', max_length=16, verbose_name='Meat')),
                ('quantity', models.IntegerField(default=1, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('time', models.IntegerField(verbose_name='time need to be done')),
                ('tem', models.IntegerField(verbose_name='temperature')),
                ('inter', models.CharField(max_length=256, verbose_name='materials needed')),
                ('img', models.FileField(max_length=128, upload_to='Menu/', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg', models.CharField(default='coriander', max_length=16, verbose_name='vegetable')),
                ('quantity', models.IntegerField(default=1, verbose_name='Amount')),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('temperature', models.IntegerField(default=0, verbose_name='Temperature')),
                ('time', models.IntegerField(verbose_name='Time')),
                ('utensils', models.CharField(max_length=128, verbose_name='Utensils')),
                ('cate', models.SmallIntegerField(choices=[(1, 'Most popular'), (2, 'Best taste'), (3, 'Vegetarianism'), (4, 'Gorgeous'), (5, 'Fast speed'), (6, 'Breakfast'), (7, 'Homely recipes'), (8, 'Baking'), (9, "Children's food"), (10, 'Baking'), (11, 'Stape Food'), (12, 'Dessert'), (13, 'Snack'), (14, 'Western Food')], default=1, verbose_name='Category')),
                ('description', models.TextField(default='Delicious', max_length=256, verbose_name='Description')),
                ('quan', models.IntegerField(default=1, verbose_name='Amount')),
                ('steps', models.TextField(max_length=500, verbose_name='Steps')),
                ('rate', models.IntegerField(choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')], default=3, verbose_name='Rate')),
                ('calories', models.DecimalField(decimal_places=2, default=300, max_digits=6, verbose_name='Calories')),
                ('img', models.FileField(default='Menu/10.jpeg', max_length=128, upload_to='Menu/', verbose_name='Logo')),
                ('auxiliary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.auxiliary')),
                ('meat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.meat')),
                ('veg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.vegetable')),
            ],
        ),
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('temperature', models.IntegerField(default=0, verbose_name='Temperature')),
                ('time', models.IntegerField(verbose_name='Time')),
                ('utensils', models.CharField(max_length=128, verbose_name='Utensils')),
                ('cate', models.SmallIntegerField(choices=[(1, 'Most popular'), (2, 'Best taste'), (3, 'Vegetarianism'), (4, 'Gorgeous'), (5, 'Fast speed'), (6, 'Breakfast'), (7, 'Homely recipes'), (8, 'Baking'), (9, "Children's food"), (10, 'Baking'), (11, 'Stape Food'), (12, 'Dessert'), (13, 'Snack'), (14, 'Western Food')], default=1, verbose_name='Category')),
                ('description', models.TextField(default='Delicious', max_length=256, verbose_name='Description')),
                ('quan', models.IntegerField(default=1, verbose_name='Amount')),
                ('steps', models.TextField(max_length=500, verbose_name='Steps')),
                ('rate', models.IntegerField(choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')], default=3, verbose_name='Rate')),
                ('calories', models.DecimalField(decimal_places=2, default=300, max_digits=6, verbose_name='Calories')),
                ('img', models.FileField(default='Menu/10.jpeg', max_length=128, upload_to='Menu/', verbose_name='Logo')),
                ('auxiliary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.auxiliary')),
                ('meat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.meat')),
                ('veg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.vegetable')),
            ],
        ),
        migrations.CreateModel(
            name='cust_recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('temperature', models.IntegerField(default=0, verbose_name='Temperature')),
                ('time', models.IntegerField(verbose_name='Time')),
                ('utensils', models.CharField(max_length=128, verbose_name='Utensils')),
                ('cate', models.SmallIntegerField(choices=[(1, 'Most popular'), (2, 'Best taste'), (3, 'Vegetarianism'), (4, 'Gorgeous'), (5, 'Fast speed'), (6, 'Breakfast'), (7, 'Homely recipes'), (8, 'Baking'), (9, "Children's food"), (10, 'Baking'), (11, 'Stape Food'), (12, 'Dessert'), (13, 'Snack'), (14, 'Western Food')], default=1, verbose_name='Category')),
                ('description', models.TextField(default='Delicious', max_length=256, verbose_name='Description')),
                ('quan', models.IntegerField(default=1, verbose_name='Amount')),
                ('steps', models.TextField(max_length=500, verbose_name='Steps')),
                ('rate', models.IntegerField(choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')], default=3, verbose_name='Rate')),
                ('calories', models.DecimalField(decimal_places=2, default=300, max_digits=6, verbose_name='Calories')),
                ('img', models.FileField(default='Menu/10.jpeg', max_length=128, upload_to='Menu/', verbose_name='Logo')),
                ('auxiliary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.auxiliary')),
                ('meat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.meat')),
                ('veg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.vegetable')),
            ],
        ),
    ]