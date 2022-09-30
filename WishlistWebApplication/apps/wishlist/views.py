from django.shortcuts import render, redirect
# from django.views.generic.list import ListView
from .models import Wish
from .forms import WishesForm


def devhome_view(request):
    return render(request, 'home.html')


def wish_create_view(request):
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
            form.save_m2m()

    context['form'] = form
    context['wishes'] = wishes
    return render(request, 'wishlist/wish_create.html', context=context)


def description_view(request):
    """Вызов описания конкретного пожелания-заметки"""
    context = {}
    if request.method == 'GET':
        wish = request.GET.get('wish')
        wish_object = Wish.objects.all().filter(wish, user_id=request.user.pk)
        description = wish_object[0].description
        image = wish_object[0].image
        context['wish'] = wish
        context['description'] = description
        context['image'] = image

    return render(request, 'wishlist/description.html', context)


def remove_wish(request):
    """Удаление заметки из вишлиста"""
    # context = {}
    if request.method == "POST":
        wish_object = Wish.objects.all().filter(wish=request.POST['delete'], user_id=request.user.pk)
        wish_object.delete()
    return redirect('/pie/')


def _add_description_image(self, id: [int]):
    """Добавление изображения в описание заметки"""
    pass


def _add_description_text(description: [str]):
    """Добавление описания к конкретной заметке"""
    pass


def _remove_description_image():
    """Удаление картинки из описания заметки"""
    pass


def _remove_description_text():
    """Удаление текста из описания заметки"""
    pass


