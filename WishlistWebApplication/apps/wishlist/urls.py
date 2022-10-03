from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    wish_create_view,
    devhome_view,
    remove_wish,
    description_view,
    add_description_image_view,
    remove_description_image,
    remove_description_text,
    add_image_view
)


urlpatterns = [
    path('', wish_create_view),
    path('test/', add_image_view),
    path('wish-remove/', remove_wish),
    path('<int:id>/', description_view),
    path('<int:id>/add-image/', add_description_image_view), # ссылка на форму добавления фотографии, ее кроп
    path('<int:id>/remove-image/', remove_description_image), # кнопка удаления фотографии
    path('<int:id>/remove-description/', remove_description_text), # кнопка удаления описания
    path('home/', devhome_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

