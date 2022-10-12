from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings

from account.models import Account
from friend.models import FriendList
from .models import Wish
from .forms import (
    WishesForm,
    DescriptionForm,
    )


def wish_create_view(request, *args, **kwargs):
    """
    Главная страница каждого пользователя
    Здесь пользователь заполняет вишлист и может
    удалить или изменить описание своих желаний
    """
    if not request.user.is_authenticated:
        raise Exception('AUTH PLEASE')
    context = {}
    wishes = Wish.objects.all().filter(user_id=request.user.pk)
    form = WishesForm()

    if request.method == "POST":
        form = WishesForm(request.POST)
        if form.is_valid():
            wish_obj = form.save(commit=False)
            wish_obj.user = request.user
            wish_obj.save()

    context['form'] = form
    context['wishes'] = wishes
    return render(request, 'wishlist/wish_create.html', context=context)


def wishlist_view(request, *args, **kwargs):
    """
    Отображение вишлиста друзьям пользователя
    """
    context = {}
    user_id = kwargs.get("user_id")

    try:
        # получаем данные аккаунта для верификации дружбы
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        # наполняем контекст данными друга (лишнее выкинуть)
        context['id'] = account.id
        context['username'] = account.username
        context['name'] = account.name
        context['surname'] = account.surname
        context['bio'] = account.bio
        # получаем френдлист друга для проверки на подтверждённую дружбу
        friend_list = FriendList.objects.get(user=account)

        # получаем друзей
        friends = friend_list.friends.all()
        context['friends'] = friends
        # Define template variables
        # выводим дефолтные значения переменных для управления шаблоном
        is_self = True
        is_friend = False
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
            if friends.filter(pk=user.id):
                is_friend = True
                # получаем список желаний друга
                wishes = Wish.objects.all().filter(user_id=user_id)
                context['wishes'] = wishes

            else:
                is_friend = False
        elif not user.is_authenticated:
            is_self = False
        else:
            HttpResponse("Smth wrong")
        # Set the template variables to the values
        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['BASE_URL'] = settings.BASE_URL
    return render(request, "wishlist/wishlist.html", context)


def wish_remove(request):
    """
    Удаление заметки из вишлиста
    """
    if request.method == "POST":
        wish_object = Wish.objects.get(pk=request.POST['delete'])
        wish_object.delete()
    return redirect("wishes:list", request.user.id)


def description_view(request, id: int):
    """
    Вызов описания конкретного пожелания-заметки
    """
    context = {}
    wish_object = Wish.objects.all().filter(pk=id)
    # id of wish owner
    user_id = wish_object[0].user_id
    try:
        # получаем данные аккаунта для верификации дружбы
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        friend_list = FriendList.objects.get(user=account)
        friends = friend_list.friends.all()
        is_self = True
        is_friend = False
        user = request.user
        if user.is_authenticated and user != account:
            is_self = False
            if friends.filter(pk=user.id):
                is_friend = True
                context['user_id'] = user_id
            else:
                is_friend = False
        elif not user.is_authenticated:
            is_self = False
        else:
            HttpResponse("Smth wrong")
            # Set the template variables to the values
        if request.method == "POST":
            form = DescriptionForm(request.POST, instance=request.user)
            if form.is_valid():
                Wish.objects.filter(pk=id).update(
                    description=form.cleaned_data['description']
                )
                form.save()
        form = DescriptionForm
        wish_name = wish_object[0].wish
        description = wish_object[0].description

        context['is_self'] = is_self
        context['is_friend'] = is_friend
        context['wish'] = wish_name
        context['description'] = description
        context['form'] = form
        context['id'] = id
    return render(request, 'wishlist/description.html', context)


def description_remove_text(request, id: int):
    """
    Удаление текста из описания заметки
    """
    if request.method == "POST":
        wish_object = Wish.objects.get(pk=request.POST['delete'])
        wish_object.description = ''
        wish_object.save()
    return redirect("wishes:list", id)


# Функция зарезервирована для управления
# фотографией внутри описания в будущем
# def add_description_image_view(request, id: int):
#     """Добавление изображения в описание заметки"""
#     context = {}
#     wish_object = Wish.objects.get(pk=id)
#     image = wish_object.image
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             wish_object.image = form.cleaned_data['image']
#             wish_object.save()
#             form.save()
#             context['image'] = image
#             context['form'] = form
#     else:
#         form = ImageForm(request.POST, request.FILES, instance=request.user)
#         context['form'] = form
#         context['image'] = image
#         context['id'] = id
#     return render(request, 'wishlist/add_image.html', context)


# Функция зарезервирована для управления
# фотографией внутри описания в будущем
# def remove_description_image(request, id: int):
#     """Удаление картинки из описания заметки"""
#     if request.method == "POST":
#         wish_object = Wish.objects.get(pk=request.POST['delete'])
#         wish_object.image.delete()
#     return redirect('wishes')
