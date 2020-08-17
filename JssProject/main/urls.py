from django.urls import path
from .views import index, create, detail, delete, update

urlpatterns = [

    path('', index, name="index"),
    path('create/', create, name="create"),
    path('detail/<int:jss_id>', detail, name="detail"),
    path('delete/<int:jss_id>', delete, name="delete"),
    path('update/<int:jss_id>', update, name="update"),
]