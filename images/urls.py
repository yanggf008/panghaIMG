from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "images"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:image_id>/add/', views.add, name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)