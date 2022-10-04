from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .services import get_random_profile_image


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address!")
        if not username:
            raise ValueError("User must have an username!")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.set_password(raw_password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, *args, **kwargs):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return f'profile_images/default/{get_random_profile_image}'


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(verbose_name='username', max_length=30, unique=True)
    name = models.CharField(verbose_name='first name', blank=True, max_length=30)
    surname = models.CharField(verbose_name='surname', blank=True, max_length=30)
    bio = models.CharField(verbose_name='bio', blank=True, max_length=100)
    dob = models.DateField(auto_now_add=True)
    join_date = models.DateTimeField(verbose_name='join date', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True,
                                      default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
# REQUIRED_FIELD это обязательное поле будет запрошено при регистрации нового пользователя
# важно сделать перенаправление на страницу профиля для заполнения профиля после регистрации пользователя

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

