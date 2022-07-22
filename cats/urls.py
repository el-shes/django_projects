from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [
    path('', views.CatsListView.as_view(), name='all_cats'),
    path('main/create/', views.CatsCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatsUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatsDelete.as_view(), name='cat_delete'),
    path('lookup/', views.BreedsListView.as_view(), name='breeds_list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]
