from django.urls import path
from .views import account_view, edit_account_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'account'

urlpatterns = [
	path('<int:user_id>/', account_view, name="view"),
	path('<int:user_id>/edit/', edit_account_view, name="edit"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
