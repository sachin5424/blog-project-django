from django.urls import path
from .views import \
    Categories_Create,Categories_List,Categories_update_and_delete,Blog_Create,Blog_List,\
    Blog_update_and_delete,HelloView,Users_Create,verfiy_user



urlpatterns = [
    path('categorie-create',Categories_Create.as_view()),
    path('categorie-list',Categories_List.as_view()),
    path('categorie/<int:pk>',Categories_update_and_delete.as_view()),
    path('blog-create',Blog_Create.as_view()),
    path('blog-list',Blog_List.as_view()),
    path('user',Users_Create.as_view()),
    path('user-verfiy',verfiy_user),
    path('blog/<int:pk>',Blog_update_and_delete.as_view()),
    path('hello', HelloView.as_view(), name='hello'),

]
