# Generated by Django 4.1.7 on 2024-07-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_canteen_food_foodcategory_order_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='foods',
            field=models.ManyToManyField(related_name='categories', to='base.food'),
        ),
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ManyToManyField(related_name='foods_in_category', to='base.foodcategory'),
        ),
    ]
