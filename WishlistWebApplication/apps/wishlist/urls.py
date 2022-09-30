from django.urls import path
from .views import (
    wish_create_view,
    devhome_view,
    remove_wish,
    description_view
)


urlpatterns = [
    path('', wish_create_view),
    path('wish-remove/', remove_wish),
    path(r'^wish/$', description_view),
    path('home/', devhome_view),
]

