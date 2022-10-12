from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    wish_create_view,
    wish_remove,
    description_view,
    description_remove_text,
    wishlist_view
    )


app_name = 'wishlist'

urlpatterns = [
    path('list/<user_id>', wish_create_view, name='list'),
    path('wishlist/<user_id>', wishlist_view, name='friend_wishlist'),
    path('wish-remove/', wish_remove, name='remove_wish'),
    path('<int:id>/', description_view, name='description'),
    path('<int:id>/remove-description/', description_remove_text, name='remove_description_text'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

