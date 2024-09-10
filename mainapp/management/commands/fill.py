from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authapp.models import ShopUser
import json, os

JSON_PATH = 'mainapp/json'


class Command(BaseCommand):
  def handle(self, *args, **options):
   

# Создаем суперпользователя при помощи менеджера модели
    super_user = ShopUser.objects.create_superuser('root','django@geekshop.local', 'root')
