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

from wishlist.views import devhome_view

from .apps.account.views import (
    index_view,
    register_view,
    login_view,
    logout_view,
    account_search_view,
)

# комментарии содержат мои пути, которые я решил определить в дизайне проекта
urlpatterns = [
    path('', index_view, name='index'),
    # -index.html в директории templates
    # На данной странице расположена краткая информация о приложении,
    # форма (или всплывающее окно) входа/регистрации, красивые картинки
    
    path('pie/', include('wishlist.urls'), name='pie'),
    # -home.html в templates.wishlist "wish_create" сейчас
    # Домашняя страница каждого юзера (редирект после входа в приложение),
    # где пользователь выполняет операции CRUD с своим вишлистом

    # path('/friends/', friendlist_view, name='friends'), -friends.html в templates.friends
    # Страница со списком друзей, виджетом поиска по имени пользователя.
    # Отсюда можно отправить заявку на принятие в друзья.

    # path('/profile/', profile_view, name='profile'), profile.html в templates.account
    # Страница личных данных пользователя с функционалом изменения или добавления
    # био, ссылок на соцсети, фото профиля, юзернейма и так далее

    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),

    # Урлы по изменению пароля можно отрефачить для лучшей наглядности
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
         name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
         name='password_change'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', account_search_view, name='search'),

    path('home/', devhome_view, name='home'),
    path('account/', include('account.urls', namespace='account')),
    # Здесь зададан путь, указывающий на урлы внутри приложения вишлиста
    # path('', include('wishlist.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
