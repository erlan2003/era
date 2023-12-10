from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

REGION_CHOICES = (
    ('osh', 'Ош'),
    ('batken', 'Баткен'),
    ('narun', 'Нарын'),
    ('ussuk-kol', 'Ыссык-Кол'),
    ('jalal-abad', 'Жалал-Абад'),
    ('chui', 'Чуй'),
    ('talas', 'Талас'),
    ('bishkek', 'Бишкек'),
)

ATTRACTION_TYPE_CHOICES = (
    ('statue', 'Статуя'),
    ('history_place', 'Историческое место'),
    ('natural_beauty', 'Природная красота'),
    ('entertainment_complexes', 'Развлекательный комплекс'),
    ('religious_place', 'Религиозная место'),
    ('technical_advances', 'Технические достижения'),
)

class Attraction(models.Model):
    attraction = models.CharField('Достопримечательность', max_length=50)
    attraction_type = models.CharField('Тип достопримечательности', max_length=50)
    region = models.CharField('Регион', max_length=50)
    information = models.TextField('Информация')

    def __str__(self):
        return self.attraction

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'



class Comment(models.Model):
    user = models.CharField('Пользователь', max_length=50)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='comments')
    subject = models.CharField('Тема', max_length=100)
    message = models.TextField('Сообщение', max_length=500)
    published = models.BooleanField('Опубликован', default=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

@receiver(post_save, sender=Comment)
def send_comment_notification(sender, instance, **kwargs):
    subject = 'Новый комментарий на вашем сайте'
    message = f'Пользователь {instance.user} оставил новый комментарий: {instance.message}'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = 'erlankudajberdiev2@gmail.com'  # Замените на свой адрес электронной почты
    send_mail(subject, message, from_email, [to_email])