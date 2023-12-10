# Generated by Django 4.2.7 on 2023-11-26 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction', models.CharField(max_length=50, verbose_name='Достопримечательность')),
                ('attraction_type', models.CharField(choices=[('statue', 'Статуя'), ('history_place', 'Историческое место'), ('natural_beauty', 'Природная красота'), ('entertainment_complexes', 'Развлекательный комплекс'), ('religious_place', 'Религиозная место'), ('technical_advances', 'Технические достижения')], max_length=50, verbose_name='Тип достопримечательности')),
                ('region', models.CharField(choices=[('osh', 'Ош'), ('batken', 'Баткен'), ('narun', 'Нарын'), ('ussuk-kol', 'Ыссык-Кол'), ('jalal-abad', 'Жалал-Абад'), ('chui', 'Чуй'), ('talas', 'Талас'), ('bishkek', 'Бишкек')], max_length=50, verbose_name='Регион')),
                ('information', models.TextField(verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.TextField(max_length=500, verbose_name='Сообщение')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.attraction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
