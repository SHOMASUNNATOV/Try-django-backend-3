from django.urls import path
from .views import recipe_list, recipe_detail,recipe_create,recipe_update,recipe_delete,tag_create,tag_detail,\
    tag_delete,tag_update,tag_list,ing_create

app_name = 'recipes'

urlpatterns = [
    path('list/', recipe_list, name='list'),
    path('detail/<slug:slug>/ ', recipe_detail, name='detail'),
    path('create/', recipe_create, name='create'),
    path('update/<slug:slug>/', recipe_update, name='update'),
    path('delete/<slug:slug>/', recipe_delete, name='delete'),

    path('tag/list/', tag_list, name='tag_list'),
    path('tag/create/ ', tag_create, name='tag_create'),
    path('tag/detail/<int:pk>/', tag_detail, name='tag_detail'),
    path('tag/update/<int:pk>/', tag_update, name='tag_update'),
    path('tag/delete/<int:pk>/ ', tag_delete, name='tag_delete'),


    path('recipe/<slug:recipe_slug>/ing/create', ing_create , name='ing_create  '),

]