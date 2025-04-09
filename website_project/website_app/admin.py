from django.contrib import admin
from .models import Users, Works

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password", "date_joined", "country")
    search_fields = ['username', 'email']
class StartupsAdmin(admin.ModelAdmin):
    list_display = ("user", "name")

admin.site.register(Users, UsersAdmin)
admin.site.register(Works, StartupsAdmin)


