from django.shortcuts import render, redirect, HttpResponse

from .models import Wish
from .forms import (
    WishesForm,
    DescriptionForm,
    ImageForm,
    TestImageForm,
)


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

    context['form'] = form
    context['wishes'] = wishes
    return render(request, 'wishlist/wish_create.html', context=context)


def description_view(request, id: int):
    """Вызов описания конкретного пожелания-заметки"""
    context = {}
    form = DescriptionForm
    wish_object = Wish.objects.all().filter(pk=id)
    if request.method == "POST":
        form = DescriptionForm(request.POST, instance=request.user)
        if form.is_valid():
            Wish.objects.filter(pk=id).update(description=form.cleaned_data['description'])
            form.save()
    wish_name = wish_object[0].wish
    description = wish_object[0].description
    image = wish_object[0].image
    context['wish'] = wish_name
    context['description'] = description
    context['image'] = image
    context['form'] = form
    return render(request, 'wishlist/description.html', context)


def remove_wish(request):
    """Удаление заметки из вишлиста"""
    if request.method == "POST":
        wish_object = Wish.objects.get(pk=request.POST['delete'])
        wish_object.delete()
    return redirect('/pie/')


def add_description_image_view(request, id: int):
    """Добавление изображения в описание заметки"""
    context = {}
    wish_object = Wish.objects.get(pk=id)
    image = wish_object.image
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            wish_object.image = form.cleaned_data['image']
            wish_object.save()
            form.save()
            context['image'] = image
            context['form'] = form
    else:
        form = ImageForm(request.POST, request.FILES, instance=request.user)
        context['form'] = form
        context['image'] = image
        context['id'] = id
    return render(request, 'wishlist/add_image.html', context)


# test definition
def add_image_view(request):
    if request.method == "POST":
        form = TestImageForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.user.id
            obj.save()
            img = Wish.objects.all().filter(user_id=request.user)
            return render(request, 'test.html', {'form': form, 'img': img})
    else:
        form = TestImageForm(initial={
            'wish': request.POST['wish'],
            'description': request.POST['description'],
            'image': request.FILES
        })
        return render(request, 'test.html', {'form': form})
    return HttpResponse('vse snova')


def remove_description_image(request, id: int):
    """Удаление картинки из описания заметки"""
    if request.method == "POST":
        wish_object = Wish.objects.get(pk=request.POST['delete'])
        wish_object.image.delete()
    return redirect('/pie/')


def remove_description_text(request):
    """Удаление текста из описания заметки"""
    if request.method == "POST":
        wish_object = Wish.objects.get(pk=request.POST['delete'])
        wish_object.description.delete()
    return redirect('/pie/')


