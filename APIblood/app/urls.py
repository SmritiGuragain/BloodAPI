from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.infosis),
    path('update/<int:pk>', views.update_info),
    path('delete/<int:pk>', views.delete_info),
]