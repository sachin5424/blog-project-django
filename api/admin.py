from django.contrib import admin
from .models import Blog,Categories,Verfiy_user
# Register your models here.


admin.site.register(Categories)

@admin.register(Blog)
class Categories_admin(admin.ModelAdmin):
    list_display = ['id','Blog_categories','Blog_title','is_Active','is_Featured']


@admin.register(Verfiy_user)
class Verfiy_user_admin(admin.ModelAdmin):
    list_display = ['id','user']
