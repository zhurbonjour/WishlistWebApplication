"""WishlistWebApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .apps.account.views import (
    index_view,
    register_view,
    login_view,
    logout_view,
    account_search_view,
)


urlpatterns = [
    path('', index_view, name='index'),
    # -index.html в директории templates
    # Страница входа или регистрации пользователя
    
    path('wishes/', include('wishlist.urls', namespace='wishes')),
    # Домашняя страница каждого юзера (редирект после входа в приложение),
    # где пользователь выполняет операции CRUD с своим вишлистом

    path('/friends/', include('friend.urls', namespace='friends')),
    # Страница со списком друзей, виджетом поиска по имени пользователя.
    # Отсюда можно отправить заявку на принятие в друзья.

    path('account/', include('account.urls', namespace='account')),
    # Страница личных данных пользователя с функционалом изменения или добавления
    # био, ссылок на соцсети, фото профиля, юзернейма и так далее

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
         name='password_change'),
    # Страница смены пароля пользователем в рамках редактирования личных данных

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', account_search_view, name='search'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
