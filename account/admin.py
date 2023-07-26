from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser

admin.site.register(CustomUser)

# admin.site.register(CustomUser, UserAdmin)


